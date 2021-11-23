import os,csv

path_data = 'path_data.csv'

def _data_writer(file,path):
    """ internal processesing"""

    with open(path_data,'a') as file_data:
        csv_writer = csv.writer(file_data)
        csv_writer.writerow([file.upper(),path])

def _data_deleter(file,path):
    """ internal processing""" 
    pass

def _locator(filename):

    """opens the file location"""
    
    file_path = None
    
    with open(path_data,'r') as file_path_data:
        csv_reader = csv.reader(file_path_data)
        
        for file_data in csv_reader:
            
            if filename in file_data:
                file_path = file_data[-1]
                file_future = os.listdir(file_data[-1])
                FILE_FUTURE = []
                
                for file in file_future:
                    FILE_FUTURE.append(file.upper())
                    
                del file_future
                
                if filename in FILE_FUTURE:
                    
                    os.startfile(file_data[-1]+'/'+filename)
                else:
                    if filename !='':
                        print('{} file have been renamed (or) deleted'.format(filename))
                        break
        return file_path
                

def goto(filename = '',root_file = 'C:/'):
    
    """ This function opens the file/exe stored at any location
        on C drive, just pass the filename with extension.

        filename:
            name of the filename.

        root_file:
        
            when your running PyNavigator for the
            first time set root_file to a root folder
            where all the subfolders are stored &
            run the programm.

            The moment you run the programm,it prints.

                Collecting path data......one time process.

            This may take some time to complete,but this is
            a one time process,so no need to worry about it.

            After the successful execution,Completed... message
            will be printed.
            
            Now, your ready to go if PyNavigator had created path_data.csv
            on your current working dir ,This is the file that contains all
            the subfolders name and path stored in you root_file folder.

            Note: Don't rename the path_data.csv file.


            just run the folllowing command:

                import PyNavigator

                PyNavigator.goto()

                when you run the following programm PyNavigator
                starts to collects all the path and filename stored
                in c drive.

            if you want to open the file/folder/exe stored in a perticuler file
            just procede as follows.

            Example for the above instruction:

                import PyNavigator

                PyNavigator.goto(root_file = r'C:\......\Desktop')

                when you run the following programm,PyNavigator
                will write all the subfolders name and path which
                are located on Desktop into path_data.csv file.

                once the path_data.csv has been created ,no need
                to use the root_file argument in any of your project,
                only if path_data.csv exist in your current working dir
                if not exists follow the above instruction.

    """
    
    try:
        return _locator(filename.upper())
    
    except:
        print("Collecting path data... ,please wait for a while.\nIt's a one time process.")
        for root,dirs,files in os.walk(root_file):
            
            for file in files:
                _data_writer(file,root)
                
            for dirc in dirs:
                if len(dirc)!=0:
                    _data_writer(dirc,root)

        print('\nCompleted...')
        if filename !='':
            goto(filename.upper())

def add_path(filename,path):
    """ add new filename and it's path.

        the user should feed the filename and path which are installed or
        created newly on the system.
    """
    
    _data_writer(filename.upper(),path)
