import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import datetime
import time

import Script_GUI_Challenge


def selectFolder1(self):
    #call a dialog that users can use to select a directory, put it in the first entry box
    self.askfile = filedialog.askdirectory()
    self.browse1.insert(END, self.askfile)

def selectFolder2(self):
    #call a dialog that users can use to select a directory, put it in the second entry box
    self.askfile = filedialog.askdirectory()
    self.browse2.insert(END, self.askfile)


def checkFolderStatus(self):
    #this code should check to see if the files were created or modified in the last 24 hours
    source = self.browse1.get('1.0', 'end') #get the input from th GUI and put it in 'source'
    files = os.listdir(source) #get a list of the files in the selected directory and put the list in 'files'
    for i in files: #iterate through the files
        getPath = os.path.abspath(i) #get the file path for each file
        modTime = os.path.getmtime(getPath)#check to see the modification time of each file
        


        #if the modification time is in the last 24 hours, move it
        #if it's not, do nothing
        
        



    

def copyFiles(self):  
    #the source folder that is selected
    source = self.browse1.get('1.0', 'end')

    #the destination folder that is selected
    destination = self.browse2.get('1.0', 'end')
    
    files = os.listdir(source)
    for i in files:
        #copy the files represented by 'i' to the destination
        shutil.copy(source+i, destination)


def endProgram(self):
        self.master.destroy()


if __name__ == "__main__":
    pass

