import tkinter as tk
from tkinter import *
import sched
import time

import Script_GUI_Challenge_func


class ParentWindow(Frame):
    def __init__ (self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)


        win.title("Check files")
        win.geometry("{}x{}".format(520,150))

        self.b1 = tk.Button(win, width=12, text="Browse Source...", command=lambda: Script_GUI_Challenge_func.selectFolder1(self))
        self.b2 = tk.Button(win, width=12, text="Browse Destination...", command=lambda: Script_GUI_Challenge_func.selectFolder2(self))
        self.b3 = tk.Button(win, width=12, height=2, text="Copy Files", command=lambda: Script_GUI_Challenge_func.copyFiles(self))
        self.b4 = tk.Button(win, height=2, text="Close Program", command=lambda: Script_GUI_Challenge_func.endProgram(self))

        self.b1.grid(row=1, column=0, padx=(15,0), pady=(35,0), sticky=W)
        self.b2.grid(row=2, column=0, padx=(15,0), pady=(10,0), sticky=W)
        self.b3.grid(row=3, column=0, padx=(15,0), pady=(10,10), sticky=W)
        self.b4.grid(row=3, column=1, padx=(10,0), pady=(10,10), sticky=E)

        self.browse1 = tk.Entry(win, width=50, text='')
        self.browse1.grid(row=0, column=1, rowspan=3, padx=(15,0), pady=(10,10), sticky=E)

        self.browse2 = tk.Entry(win, width=50,  text='')
        self.browse2.grid(row=1, column=1, rowspan=3, padx=(15,0), pady=(10,10), sticky=E)

if __name__ == "__main__":
    sched.every().day.at("05:00").do(checkFolderStatus) #this calls the checkfolder status function every day at 5 AM
    win = tk.Tk() #this is the syntax to call a tkinter window, put in the variable win
    App = ParentWindow(win) #instantiating a class of ParentWindow called "App"
    win.mainloop() #keep the window open



