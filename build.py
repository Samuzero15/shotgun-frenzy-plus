
import os
import sys
import subprocess
import zipfile
import funs_n_cons as utils

from argparse import ArgumentParser
from configparser import ConfigParser

if __name__ == "__main__":
    command = "cd"
    
    cmd = ArgumentParser()
    cmd.add_argument("-d", "--dist", action="store_true", dest="dist", default=False, help="Make a versioned build")
    cmd.add_argument("-xr", "--exres", action="store_true", dest="nores", default=False, help="Dont build the resource part")
    cmd.add_argument("-xm", "--exmus", action="store_true", dest="nomus", default=False, help="Dont build the music part")
    cmd.add_argument("-xrm", "--justcore", action="store_true", dest="justcore", default=False, help="Skips resources and music parts, zipping only the core")
    args = cmd.parse_args()

    config = ConfigParser()
    config.read("project.ini")
    
    if(len(config.sections()) == 0):
        print("Hm...It seems there is no project over here. Maybe you did'nt configured the project.ini file.")
        sys.exit();
    
    exe_path    = config["Executable"].get('zandronum_path', '?');
    std_path    = config["Executable"].get('skulldata_path', '?');
    
    # Check for relative paths. (use ..\ for a relative path.)
    if('..\\' in exe_path):
        exe_path = utils.relativePath(exe_path)
        
    if('..\\' in std_path):
        std_path = utils.relativePath(std_path)
    
    # Check if the file exist.
    if(not os.path.isfile(os.path.join(exe_path, utils.EXE_FNAME))):
        print("Zandronum executable path does not exist, go fix that in the project.ini file.");
        sys.exit();
        
    if(not os.path.isfile(os.path.join(std_path, utils.STD_FNAME))):
        print("Skulltag Content file does not exist, go fix that in the project.ini file.");
        sys.exit();
    else: 
        std_path += '\\' + utils.STD_FNAME;
    
    # print(utils.print_showcase_changes(True))
    # sys.exit()
    
    rootDir = os.getcwd()
    
    filelist = []

    for part in config.sections():
        if part != "Executable":
            relase    = config[part].get('relase'   , 'v0'   );
            sourceDir = config[part].get('SourceDir', 'src'  );
            distDir   = config[part].get('DistDir'  , 'dist' );
            fileName  = config[part].get('FileName' , part   );
            notxt     = config[part].get('notxt'    , False  );
            compileacs= bool(config[part].get('compile_acs', False));

            destPath = os.path.join(distDir, fileName)
            
            if (part == "Resources"):
                if(args.dist):
                    res_file = fileName + "_" + relase + ".pk3"
                    res_file_path = destPath + "_" + relase + ".pk3"
                else:
                    res_file = fileName + ".pk3"
                    res_file_path = destPath + ".pk3"
                
                # Check for the arguments. 
                coreonly = (args.justcore or (args.nores and args.nomus))
                if (coreonly and ("Resources" in part or "Music" in part)):
                    print ("\n-- Resources and Music parts excluded --")
                    if(not os.path.isfile(os.path.join(os.getcwd(), res_file_path))):
                        print ("-- There is not even a file called: " + res_file + " as resource part... --")
                        print ("-- Run aborted, try 'python build.py [-d]' to generate the resource part --")
                        sys.exit()
                    else:
                        print ("-- Using: " + res_file + " as resource part --")
                    filelist.append(os.path.join(os.getcwd(), res_file_path));
                    break
                
                if (args.nores and part == "Resources"):
                    print ("\n-- Resources part excluded --")
                    if(not os.path.isfile(os.path.join(os.getcwd(), res_file_path))):
                        print ("-- There is not even a file called: " + res_file + " as resource part... --")
                        print ("-- Run aborted, try 'python build.py [-d]' to generate the resource part --")
                        sys.exit()
                    else:
                        print ("-- Using: " + res_file + " as resource part --")
                        
                    filelist.append(os.path.join(os.getcwd(), res_file_path));
                    continue
                
            if (args.nomus and part == "Music"):
                print ("\n-- Music part excluded --")
                continue
            

            
            print("\n-- Building {name} --".format(name=part));
            # Main stuff. 
            if not os.path.exists(distDir):
                os.mkdir(distDir)
            
            if(compileacs): 
                utils.acs_compile(rootDir, sourceDir, part)
            
            zip = utils.makepkg(sourceDir, destPath, notxt, True)
            if not notxt: 
                # For the gameinfo, buildinfo and changelog files.
                wadinfoPath = destPath + ".txt"
                if(os.path.isfile(os.path.join(sourceDir, 'GAMEINFO.txt'))):
                    # Get all writeable files and replace them with the version and time.
                    files = ['Language.txt', 'gameinfo.txt', 'changelog.md']
                    
                    for file in files:
                        source = sourceDir
                        if (file == 'changelog.md'): source = rootDir
                        utils.maketxt(source, destPath, relase, file)
                        zip.write(wadinfoPath, file)
                utils.maketxt(sourceDir, destPath, relase, "buildinfo.txt")
                zip.write(wadinfoPath, 'buildinfo.txt')
            zip.close()
            
            
            if(args.dist and not notxt):
                utils.makever(relase, destPath)
                filelist.append(os.getcwd() + '\\' + destPath + "_" + relase + '.pk3');
            else: 
                filelist.append(os.getcwd() + '\\' + destPath + '.pk3');
            
            print('-- {p} part Finished! --'.format(p=part))
    
    # Finally, run the build.
    print("\n-- Zandronum.exe will run shortly... --");
    os.chdir(exe_path);
    fullcmd     = ["zandronum.exe", "-iwad", "doom2.wad", "-file", std_path]
    subprocess.call(fullcmd + filelist)
    print("\n-- All done! Bye-Bye! --");
