# Constants and useful functions.

import os
import sys
import zipfile
import datetime
import subprocess

from glob import iglob
from shutil import copyfile

TODAY = datetime.datetime.now().strftime('%d/%m/%Y')

BAR_SIZE = 20
EXE_FNAME = "zandronum.exe"
ACC_FNAME = "acc.exe"
STD_FNAME = "skulltag_content-3.0-beta01.pk3"
EXCLUDE_FILE_EXTS = [".backup1", ".backup2", ".backup3", ".bak", ".dbs"]

#
# Build main package (as .pk3, a good ol' zip, really)
#
def makepkg(sourcePath, destPath, notxt=False, skipGameInfo=False):
    destination = destPath + ".pk3"
    wadinfoPath = destPath + ".txt" # just assume this, 'cause we can.

    print ("--> Compressing {filename}".format (filename=destination))
    filelist = []
    for path, dirs, files in os.walk (sourcePath):
        for file in files:
            if not (file_igonre(file) or file == "buildinfo.txt" or (skipGameInfo and file == "GAMEINFO.txt")): # special exceptions
            # Remove sourcepath from filenames in zip
                splitpath = path.split(os.sep)[1:]
                splitpath.append(file)
                name = os.path.join(*splitpath)
                filelist.append((os.path.join (path, file), name,))

    distzip = zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED)
    current = 1
    for file in filelist:
        printProgress (current, len(filelist), 'Zipped: ', 'files. \t(' + file[1] + ')', 1, BAR_SIZE, "--> Zipping completed!")
        distzip.write(*file)
        current += 1
    
    return (distzip)
    
def file_igonre(file):
    should_ignore = False;
    for ext in EXCLUDE_FILE_EXTS:
        if not (should_ignore): should_ignore = file.endswith(ext);
        else: break;
    return should_ignore;

def maketxt(sourcePath, destPath, version, filetemplate):
    textname = os.path.join(sourcePath, filetemplate)
    destname = destPath + ".txt"
        
    print("--> Copying {source} to {dest}".format (source=textname, dest=destname))
    sourcefile = open (textname, "rt")
    textfile = open (destname, "wt")
    for line in sourcefile:
        line = line.replace('x.x.x', version)
        line = line.replace('_DEV_', version)
        line = line.replace('XX/XX/XXXX', TODAY)
        textfile.write(line)
    
    textfile.close()
    sourcefile.close()

def makever(version, destPath):
    print("--> Making distribution version --")
    copyfile(destPath + ".pk3", destPath + "_" + version + ".pk3")
    copyfile(destPath + ".txt", destPath + "_" + version + ".txt"); 
    os.remove(destPath + ".pk3"); 
    os.remove(destPath + ".txt")

def printProgress(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, onend = " Done! ", fill = '█'):
    try:
        printProgressBar (iteration, total, prefix, suffix, decimals, length, fill,'-', onend)
    except UnicodeEncodeError:
        printProgressBar (iteration, total, prefix, suffix, decimals, length, '#' ,'0', onend)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', fore= '-', onend ='Done!', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + fore * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    
    if iteration == total: 
        print(f'{onend}')
    

def relativePath (path):
    path = os.path.join(os.getcwd(), path)
    path = path.replace('..\\', '')
    return path
    
def part_alt(config, part):
    f_name  = config[part].get('FileName', part  )
    f_distdir = config[part].get('DistDir', 'dist');
    f_destpath = os.path.join(f_distdir, f_name)
    
    file = f_name + ".pk3"
    file_path = f_destpath + ".pk3"
    # print ("\n-- " + file + " part excluded --")
    if(not os.path.isfile(os.path.join(os.getcwd(), file_path))):
        print ("-- No file called: " + file + " as "+ part +" part... --")
        return False
    else:
        print ("-- Using: " + file + " as " + part + " part --")
        return True
        
def part_alt_file(config, part):
    f_name  = config[part].get('FileName', part  )
    f_distdir = config[part].get('DistDir', 'dist');
    f_destpath = os.path.join(f_distdir, f_name)
    
    file = f_name + ".pk3"
    file_path = f_destpath + ".pk3"
    return os.path.join(os.getcwd(), file_path);
    

def acs_compile(rootDir, sourceDir, part):
        
    tools_dir = os.path.join(rootDir, "tools");
    acs_dir = os.path.join(rootDir, sourceDir, "acs");
    src_dir = os.path.join(rootDir, sourceDir, "source");
    
    includes = ['-i'] + [tools_dir] + ['-i'] + [src_dir]
    
    # print(includes);
    
    os.chdir(acs_dir);
    # Get rid of the old compiled files, for a clean build.
    print("--> Clearing old compiled ACS for {name}".format(name=part));
    current = 0;
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".o"):
               os.remove(os.path.join(root, file));
               printProgress(current, len(files), 'Cleared', '.o files. \t(' + file + ')', 1, BAR_SIZE)
               current += 1;

    print("--> Compiling ACS for {name}".format(name=part));
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
                f_names = os.path.basename(f_target).split('.')[0] + '.' + os.path.basename(f_target).split('.')[1]
                
                compcmd     = [os.path.join(tools_dir, 'acc.exe')] + includes + [f_target] + [os.path.join(acs_dir, f_name + '.o')]
                
                
                subprocess.call(compcmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                # print (includes)
                # print (os.getcwd())
                # time.sleep(1)
                current+=1;
                printProgress(current, fileslist, 'Compiled', 'acs files. \t(' + f_names + ')', 1, BAR_SIZE,  "--> ACS compiling completed!")
                acs_err = os.path.join(root, 'acs.err')
                
                if os.path.isfile(acs_err):
                    os.chdir(root);
                    os.system('cls')
                    with open('acs.err', 'rt') as errorlog:
                        print(errorlog.read())
                        errorlog.close()
                    os.remove(os.path.join(root, 'acs.err'))
                    print("\n-- Fix those errors and try again, compilation failed. --")
                    sys.exit()
                
                # Check this if the output file was'nt created.
                if not os.path.isfile(os.path.join(acs_dir, f_name + '.o')):
                    os.chdir(root);
                    os.system('cls')
                    if(os.path.isfile(acs_err)): os.remove(acs_err)
                    print("\n-- The expected file was'nt created, compilation failed. --")
                    sys.exit()
                
    os.chdir(rootDir)
