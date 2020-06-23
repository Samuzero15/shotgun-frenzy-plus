
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
		print ("[{percent:>3d}%] Adding {filename}".format(percent = int(current * 100 / len (filelist)), filename=file[1]))
		distzip.write(*file)
		current += 1

if __name__ == "__main__":

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
                            print ("[{percent:>3d}%] Compiling: {filename}".format(
                                percent = int(current * 100 / fileslist), filename=os.path.basename(f_target)))
                            subprocess.call(compcmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                            current+=1;
                            if(os.path.isfile(os.path.join(root, 'acs.err'))):
                                print(compcmd)
                                os.remove(os.path.join(root, 'acs.err'))
                                sys.exit()
                            # time.sleep(1)
                os.chdir(rootdir)
            
            print("\n-- Building {name} --".format(name=part));
            
            if not os.path.exists(distDir):
                os.mkdir(distDir)

            destPath = os.path.join(distDir, fileName)
            
            makepkg(sourceDir, destPath, notxt)
            
            filelist.append(os.getcwd() + '\\' + destPath + '.pk3');
            
            

            print("\n-- Finished! --")
    
    #print(filelist)

    exe_path    = config["Executable"].get('zandronum_path', '?');
    std_path    = config["Executable"].get('skulldata_path', '?');
    os.chdir(exe_path);
    fullcmd     = ["zandronum.exe", "-iwad", "doom2.wad", "-file", std_path]
    #print(fullcmd + filelist)
    subprocess.call(fullcmd + filelist)
    for file in filelist:
        os.remove(file)
