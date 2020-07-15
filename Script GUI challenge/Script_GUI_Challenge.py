import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("Check files")
win.geometry("{}x{}".format(520,150))
b1 = Button(win, width=12, text="Browse...")
b2 = Button(win, width=12, text="Browse...")
b3 = Button(win, width=12, height=2, text="Check for files...")
b4 = Button(win, height=2, text="Close Program")
b1.grid(row=1, column=0, padx=(15,0), pady=(35,0), sticky=W)
b2.grid(row=2, column=0, padx=(15,0), pady=(10,0), sticky=W)
b3.grid(row=3, column=0, padx=(15,0), pady=(10,10), sticky=W)
b4.grid(row=3, column=1, padx=(10,0), pady=(10,10), sticky=E)

browse1 = Entry(win, width=50, text='')
browse1.grid(row=0, column=1, rowspan=3, padx=(15,0), pady=(10,10), sticky=E)

browse2 = Entry(win, width=50,  text='')
browse2.grid(row=1, column=1, rowspan=3, padx=(15,0), pady=(10,10), sticky=E)

