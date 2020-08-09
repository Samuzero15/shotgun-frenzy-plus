
import os
import sys
import subprocess
import zipfile
import funs_n_cons as utils

from argparse import ArgumentParser
from configparser import ConfigParser
            

if __name__ == "__main__":

    cmd = ArgumentParser()
    cmd.add_argument("-s", "--save", 
        action="store_true", dest="save",
        default=False,
        help="save testing version.")
    cmd.add_argument("-xrm", "--justcore", 
        action="store_true", dest="justcore",
        default=False,
        help="skip resources and music zipping.")
    cmd.add_argument("-xr", "--skipres", 
        action="store_true", dest="nores",
        default=False,
        help="skip resources zipping.")
    cmd.add_argument("-xm", "--skipmus", 
        action="store_true", dest="nomus",
        default=False,
        help="skip music zipping.")
    args = cmd.parse_args()
    
    config = ConfigParser()
    config.read("project.ini")
    
    
    
    if(len(config.sections()) == 0):
        print("Hm...It seems there is no project over here. Maybe you did'nt configured the project.ini file.")
        sys.exit();
    
    exe_path    = config["Executable"].get('zandronum_path', '?');
    std_path    = config["Executable"].get('skulldata_path', '?');
    map_test    = config["Executable"].get('testing_map', 'MAP18');
    acc_path    = config["Executable"].get('acscomp_path', '?');
    
    # Check for relative paths. (use ..\ for a relative path.)
    if('..\\' in exe_path):
        exe_path = utils.relativePath(exe_path)
        
    if('..\\' in acc_path):
        acc_path = utils.relativePath(acc_path)
    
    if('..\\' in std_path):
        std_path = utils.relativePath(std_path)
    
    # Check if the file exist.
    if(not os.path.isfile(os.path.join(exe_path, utils.EXE_FNAME))):
        print("Zandronum executable path does not exist, go fix that in the project.ini file.");
        sys.exit();
    
    if(not os.path.isfile(os.path.join(acc_path, utils.ACC_FNAME))):
        print("ACC executable path does not exist, go fix that in the project.ini file.");
        sys.exit();
    
    if(not os.path.isfile(os.path.join(std_path, utils.STD_FNAME))):
        print("Skulltag Content file does not exist, go fix that in the project.ini file.");
        sys.exit();
    else: 
        std_path += '\\' + utils.STD_FNAME;
        
    rootdir = os.getcwd();
    
    filelist = []
    for part in config.sections():
        if part != "Executable":
            
            sourceDir =      config[part].get('SourceDir'  , 'src' );
            distDir = config["Resources"].get('DistDir', 'dist');
            fileName  =      config[part].get('FileName'   , part  );
            notxt     = bool(config[part].get('notxt'      , False));
            compileacs= bool(config[part].get('compile_acs', False));
            
            destPath = os.path.join(distDir, fileName)
            
            if (part == "Resources" or part == "Music"):
                fileName  = config["Resources"].get('FileName', part  )
                distDir = config["Resources"].get('DistDir', 'dist');
                destPath = os.path.join(distDir, fileName)
                
                res_file = fileName + ".pk3"
                res_file_path = destPath + ".pk3"
                
                fileName  = config["Music"].get('FileName', part  )
                distDir = config["Music"].get('DistDir', 'dist');
                destPath = os.path.join(distDir, fileName)
                
                mus_file = fileName + ".pk3"
                mus_file_path = destPath + ".pk3"
                
                coreonly = (args.justcore or (args.nores and args.nomus))
                if (coreonly and ("Resources" in part or "Music" in part)):
                    print ("\n-- Resources and Music parts excluded --")
                    
                    # Check for resources file
                    if(not os.path.isfile(os.path.join(os.getcwd(), res_file_path))):
                        print ("-- There is not even a file called: " + res_file + " as resource part... --")
                        print ("-- Run aborted, try 'python play.py [-s]' to generate the resource part --")
                        sys.exit()
                    else:
                        print ("-- Using: " + res_file + " as resource part --")
                        filelist.append(os.path.join(os.getcwd(), res_file_path));
                    
                    
                    # Check for music file
                    if(not os.path.isfile(os.path.join(os.getcwd(), mus_file_path))):
                        print ("-- No file: " + mus_file + " as music part... --")
                        print ("-- Run will resume, but expect a silenced game. --")  
                    else:
                        print ("-- Using: " + mus_file + " as music part --")
                        filelist.append(os.path.join(os.getcwd(), mus_file_path));
                    
                    break
                    
            # Check them separated
            if (args.nores and part == "Resources"):
                res_file = fileName + ".pk3"
                res_file_path = destPath + ".pk3"
                print ("\n-- Resources part excluded --")
                if(not os.path.isfile(os.path.join(os.getcwd(), res_file_path))):
                    print ("-- There is not even a file called: " + res_file + " as resource part... --")
                    print ("-- Run aborted, try 'python play.py [-s]' to generate the resource part --")
                    sys.exit()
                else:
                    print ("-- Using: " + res_file + " as resource part --")
                    
                filelist.append(os.path.join(os.getcwd(), res_file_path));
                continue
                
            if (args.nomus and part == "Music"):
                mus_file = fileName + ".pk3"
                mus_file_path = destPath + ".pk3"
                print ("\n-- Music part excluded --")
                if(not os.path.isfile(os.path.join(os.getcwd(), mus_file_path))):
                    print ("-- No file: " + mus_file + " as music part... --")
                    print ("-- Run will resume, but expect a silenced game. --")  
                else:
                    print ("-- Using: " + res_file + " as music part --")
                    filelist.append(os.path.join(os.getcwd(), mus_file_path));
                continue
            
            print("\n-- Building {name} --".format(name=part));
            if(compileacs): 
                utils.acs_compile(rootdir, sourceDir, part)
            
            if not os.path.exists(distDir):
                os.mkdir(distDir)
            filelist.append(os.getcwd() + '\\' + destPath + '.pk3')
            
            utils.makepkg(sourceDir, destPath, notxt)
            
            
            print("-- Finished! --")
    
    # Finally run the build
    print("\n-- Zandronum.exe will run shortly... --");
    os.chdir(exe_path);
    fullcmd     = ["zandronum.exe", "-iwad", "doom2.wad", "-file", std_path]
    subprocess.call(fullcmd + filelist + ['+map', map_test])
    if(not args.save):
        for file in filelist:
            os.remove(file)
    else: print("--> The files are saved in: " + distDir)
    print("\n-- All done! Bye-Bye! --");
