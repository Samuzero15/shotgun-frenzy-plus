
import os
import sys
import subprocess
import zipfile
import datetime

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
            if not (file == "buildinfo.txt" or file == "GAMEINFO.txt"): # special exceptions
            # Remove sourcepath from filenames in zip
                splitpath = path.split(os.sep)[1:]
                splitpath.append(file)
                name = os.path.join(*splitpath)
                filelist.append((os.path.join (path, file), name,))

    distzip = zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED)
    current = 1
    for file in filelist:
        printProgressBar (current, len(filelist), 'Zipped: ', ' files', 1, 25)
        # print ("[{percent:>3d}%] Adding {filename}".format(percent = int(current * 100 / len (filelist)), filename=file[1]))
        distzip.write(*file)
        current += 1
    
    return (distzip)
    

def maketxt(sourcePath, destPath, version, filetemplate):
    textname = os.path.join(sourcePath, filetemplate)
    destname = destPath + ".txt"
        
    print("\n-- Copying {source} to {dest} --".format (source=textname, dest=destname))
    sourcefile = open (textname, "rt")
    textfile = open (destname, "wt")
    for line in sourcefile:
        line = line.replace('x.x.x', version)
        line = line.replace('_DEV_', version)
        line = line.replace('XX/XX/XXXX', today)
        textfile.write(line)
    
    textfile.close()
    sourcefile.close()

def makever(version, destPath):

	print("\n-- Making distribution version --")

	copyfile(destPath + ".pk3", destPath + "_" + version + ".pk3")
	copyfile(destPath + ".txt", destPath + "_" + version + ".txt")

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

if __name__ == "__main__":
    command = "cd"
    
    cmd = ArgumentParser()
    cmd.add_argument("-d", "--dist", action="store_true", dest="dist", default=False, help="Make a versioned build")
    cmd.add_argument("-xr", "--exres", action="store_true", dest="nores", default=False, help="Dont build the resource part")
    cmd.add_argument("-xm", "--exmus", action="store_true", dest="nomus", default=False, help="Dont build the music part")
    args = cmd.parse_args()

    config = ConfigParser()
    config.read("project.ini")
    
    if(len(config.sections()) == 0):
        print("Hm...It seems there is no project over here. Maybe you did'nt configured the project.ini file.")
    
    filelist = []

    for part in config.sections():
        if part != "Executable":
            relase    = config[part].get('relase'   , 'v0'   );
            sourceDir = config[part].get('SourceDir', 'src'  );
            distDir   = config[part].get('DistDir'  , 'dist' );
            fileName  = config[part].get('FileName' , part   );
            notxt     = config[part].get('notxt'    , False  );

            if (args.nores and part == "Resources"):
            	continue
			
            print("\n-- Building {name} --".format(name=part));
            
            if not os.path.exists(distDir):
                os.mkdir(distDir)

            destPath = os.path.join(distDir, fileName)
            
            zip = makepkg(sourceDir, destPath, notxt)
            if not notxt: 
                wadinfoPath = destPath + ".txt"
                if(os.path.isfile(os.path.join(sourceDir, 'GAMEINFO.txt'))):
                    maketxt(sourceDir, destPath, relase, 'GAMEINFO.txt')
                    zip.write(wadinfoPath, 'GAMEINFO.txt')
                maketxt(sourceDir, destPath, relase, "buildinfo.txt")
                zip.write(wadinfoPath, 'buildinfo.txt')
            
            
            if(args.dist and not notxt):
                makever(relase, destPath)
            zip.close();
            filelist.append(os.getcwd() + '\\' + destPath + '.pk3');
            
            

        print("\n-- Finished! --")
    
    #print(filelist)

    exe_path    = config["Executable"].get('zandronum_path', '?');
    std_path    = config["Executable"].get('skulldata_path', '?');
    os.chdir(exe_path);
    fullcmd     = ["zandronum.exe", "-iwad", "doom2.wad", "-file", std_path]
    #print(fullcmd + filelist)
    subprocess.call(fullcmd + filelist)
