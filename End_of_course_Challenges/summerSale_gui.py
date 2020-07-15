import tkinter as tk
from tkinter import *
import summerSale_website
from tkinter import messagebox

class ParentWindow(Frame):
    def __init__ (self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        #basic window features
        win.title("Update Website")
        win.geometry("{}x{}".format(550,275))
        win.config(bg='coral')

        #entry box
        self.addBody = tk.Text(win, width=50, height=10)
        self.addBody.grid(row=0, column=0, columnspan=4, pady=10, sticky=S)

        #buttons
        self.b1 = tk.Button(win, width=12, height=2, wraplength=80, text="Add to site contents", command=lambda: summerSale_website.addToBody(self))
        self.b2 = tk.Button(win, width=12, height=2, wraplength=80, text="Overwrite site contents", command=lambda: summerSale_website.overwriteBody(self))
        self.b3 = tk.Button(win, width=12, height=2, wraplength=80, text="Create new site", command=lambda: summerSale_website.createSite(self))
        self.b4 = tk.Button(win, width=12, height=2, wraplength=80, text="Close Program", command=lambda: summerSale_website.endProgram(self))

        #button placement
        self.b1.grid(row=1, column=0, padx=(20,20), pady=10, sticky=W)
        self.b2.grid(row=1, column=1, padx=(20,20), pady=10, sticky=W)
        self.b3.grid(row=1, column=2, padx=(20,20), pady=10, sticky=W)
        self.b4.grid(row=1, column=3, padx=(20,20), pady=10, sticky=W)





if __name__ == "__main__":
    win = tk.Tk() #this is the syntax to call a tkinter window, put in the variable win
    App = ParentWindow(win) #instantiating a class of ParentWindow called "App"
    win.mainloop()



    
