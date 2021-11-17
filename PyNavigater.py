import os,time
from pyautogui import press,hotkey

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
        os.startfile(filename)
    except:
        return None
    


def search_start(filename):

    hotkey('ctrl','esc')
    
    time.sleep(0.2)
    
    for char in filename:
        press(char)
        
    time.sleep(0.2)
    press('enter')
