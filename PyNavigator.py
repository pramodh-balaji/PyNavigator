import os
import subprocess

def search(file,control = os.getcwd()):
    
    file_in_sys = {}

    try:

        for root ,dirs,files in os.walk(control):
            for f in files:
                file_in_sys[f] = root
            for folder in dirs:
                file_in_sys[folder] = root
            for dirc in dirs:
                file_in_sys[dirc] = root
    except:
        
        return None
    
    return file_in_sys[file]




def run(filename,path = os.getcwd()):

    try:
        os.chdir(search(filename,path))
        subprocess.run("start {}".format(filename),shell = True)
    except:
        return None

def close():
    pass
