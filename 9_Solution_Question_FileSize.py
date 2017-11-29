import os
##give the directory name below
mydir=r'C:\Users\Apf\Desktop\python-3.6.3\New folder'

def get_file_size(dirpath):
    for i in os.listdir(dirpath):
        path =os.path.join(dirpath, i)
        if os.path.isfile(path) and os.path.getsize(path)==0:
            print("File name : {0} ; Size : {1}".format(os.path.basename(path),os.path.getsize(path)))

get_file_size(mydir)
