import shutil
import os

#set where the source of the files are. Note the slash angle!
source = 'C:/Users/lenni/Desktop/FolderA/'

#set the destination path to folderB
destination = 'C:/Users/lenni/Desktop/FolderB/'
files = os.listdir(source)



for i in files:
    #move the files represented by 'i' to the destination
    shutil.move(source+i, destination)

