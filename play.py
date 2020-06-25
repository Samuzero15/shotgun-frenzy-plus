
import os
import sys
import subprocess
import zipfile
import datetime
import time

from glob import iglob
from shutil import copyfile
from argparse import ArgumentParser
from configparser import ConfigParser

today = datetime.datetime.now().strftime('%d/%m/%Y')

#
# Build main package (as .pk3, a good ol' zip, really)
#
def makepkg(sourcePath, destPath, notxt=False):
    destination = destPath + ".pk3"
    wadinfoPath = destPath + ".txt" # just assume this, 'cause we can.

    print ("\n-- Compressing {filename} --".format (filename=destination))
    filelist = []
    for path, dirs, files in os.walk (sourcePath):
        for file in files:
            if file != "buildinfo.txt": # special exception
                # Remove sourcepath from filenames in zip
                splitpath = path.split(os.sep)[1:]
                splitpath.append(file)
                name = os.path.join(*splitpath)

                filelist.append((os.path.join (path, file), name,))

    distzip = zipfile.ZipFile(destination, "w", zipfile.ZIP_STORED)
    current = 1
    for file in filelist:
        printProgressBar (current, len (filelist), 'Zipped:', 'files.', 1, 20)
        distzip.write(*file)
        current += 1

'''
    Draw a nice progress bar.
'''
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def acs_compile(rootDir, SourceDir):
        
    tools_dir = os.path.join(rootdir, "tools");
    acs_dir = os.path.join(rootdir, sourceDir, "acs");
    src_dir = os.path.join(rootdir, sourceDir, "source");
    includes = ['-i'] + [tools_dir] + ['-i'] + [src_dir]
    
    # print(includes);
    
    os.chdir(tools_dir);
    compcmd     = ["acc"] + includes
    
    print("\n--Compiling ACS for {name} --".format(name=part));
    os.chdir(src_dir);
    
    fileslist = 0;
    for root, dirs, files in os.walk(os.getcwd()):
        for dir in dirs:
            # print(os.path.join(root, dir))
            includes = includes + ['-i'] + [os.path.join(root, dir)]
        
        for file in files:
            if file.endswith(".acs"):
                fileslist+=1
    
    current = 0;
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            
            if file.endswith(".acs"):
                f_target = os.path.join(root, file)
                f_name = os.path.basename(f_target).split('.')[0]
                compcmd     = ["acc"] + includes + [f_target] + [os.path.join(acs_dir, f_name + '.o')]
                
                subprocess.call(compcmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                current+=1;
                printProgressBar (current, fileslist, 'Compiled', 'acs files.', 1, 20)
                if(os.path.isfile(os.path.join(root, 'acs.err'))):
                    os.chdir(root);
                    os.system('cls')
                    with open('acs.err', 'rt') as errorlog:
                        print(errorlog.read())
                        errorlog.close()
                    time.sleep(3)
                    os.remove(os.path.join(root, 'acs.err'))
                    sys.exit()
                
    os.chdir(rootdir)
            

if __name__ == "__main__":

    cmd = ArgumentParser()
    cmd.add_argument("-s", "--save", 
        action="store_true", dest="save",
        default=False,
        help="save testing version.")
    cmd.add_argument("-srm", "--skipresmus", 
        action="store_true", dest="skip_resmus",
        default=False,
        help="skip rresources and music zipping.")
    cmd.add_argument("-sr", "--skipres", 
        action="store_true", dest="skip_res",
        default=False,
        help="skip resources zipping.")
    cmd.add_argument("-sm", "--skipmus", 
        action="store_true", dest="skip_mus",
        default=False,
        help="skip music zipping.")
    args = cmd.parse_args()
    
    config = ConfigParser()
    config.read("project.ini")
    
    if(len(config.sections()) == 0):
        print("Hm...It seems there is no project over here. Maybe you did'nt configured the project.ini file.")
    
    rootdir = os.getcwd();
    
    filelist = []
    acc_path    = config["Executable"].get('acscomp_path', '?');
    for part in config.sections():
        if part != "Executable":
            
            sourceDir =      config[part].get('SourceDir'  , 'src' );
            distDir   =      config[part].get('DistDir'    , 'dist');
            fileName  =      config[part].get('FileName'   , part  );
            notxt     = bool(config[part].get('notxt'      , False));
            compileacs= bool(config[part].get('compile_acs', False));
            
            if(compileacs): 
                acs_compile(rootdir, sourceDir)
            
            print("\n-- Building {name} --".format(name=part));
            
            if not os.path.exists(distDir):
                os.mkdir(distDir)

            destPath = os.path.join(distDir, fileName)
            filelist.append(os.getcwd() + '\\' + destPath + '.pk3')
            
            if not((part == "Resources" and (args.skip_res or args.skip_resmus)) or (part == "Music" and (args.skip_mus or args.skip_resmus))):
                makepkg(sourceDir, destPath, notxt)
            else: 
                print("\n-- {name} skipped! --".format(name=part))
                continue
            
            
            print("\n-- Finished! --")
    
    #print(filelist)

    exe_path    = config["Executable"].get('zandronum_path', '?');
    std_path    = config["Executable"].get('skulldata_path', '?');
    os.chdir(exe_path);
    fullcmd     = ["zandronum.exe", "-iwad", "doom2.wad", "-file", std_path]
    subprocess.call(fullcmd + filelist + ["-map TEST"])
    if( not args.save):
        for file in filelist:
            os.remove(file)
    else: print("The files are saved in: " + distDir)
