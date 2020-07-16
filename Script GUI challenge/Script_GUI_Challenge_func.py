import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import datetime
import time
import shutil
from shutil import copyfile

import Script_GUI_Challenge


def selectFolder1(self):
    #call a dialog that users can use to select a directory, put it in the first entry box
    self.source = filedialog.askdirectory()
    self.browse1.insert(END, self.source)

def selectFolder2(self):
    #call a dialog that users can use to select a directory, put it in the second entry box
    self.destination = filedialog.askdirectory()
    self.browse2.insert(END, self.destination)


def copyFiles(self):
    files = os.listdir(self.source) #self.source is from the filedialog above
    for i in files:
        getSrcPath = os.path.join(self.source, i) #get the complete file path for the source
        getDstPath = os.path.join(self.destination, i) #get the complete file path for the destination
        modTime = os.path.getmtime(getSrcPath)#check to see the modification time of each file
        print(modTime, i) #prints the modification time and file name
        modTime_ezformat = time.ctime(modTime) #changes the modificaiton time to an easily understood format
        print(modTime_ezformat) #prints the easy format, just for me to check that it works
        now = time.time()
        print(now)
        last24 = int(now) - 68400
        last24_ezformat = time.ctime(last24)
        #Since24HoursAgo = int(modTime) - 86400 #subtracts one day from time the script is run
        #Since24HoursAgo_ezformat = time.ctime(Since24HoursAgo) #changes the 24 hrs ago to an easy format
        #print(Since24HoursAgo) #prints the time from 24 hrs ago
        #print(Since24HoursAgo_ezformat) #prints the easy format from 24 hrs ago, for me to check that it works
        
        if int(modTime) > int(last24):
            #copy the files represented by 'i' to the destination
            shutil.copyfile(getSrcPath, getDstPath)
        else:
            pass


def endProgram(self):
        self.master.destroy()


if __name__ == "__main__":
    pass

