import tkinter
from tkinter import *

# Frame is the parent class in tkinter
#You can copy/paste the next three lines
# and the bottom 4 lines for other code
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.title('Learning Tkinter!') #gives the GUI a title
        self.master.config(bg='darkgray') #sets a background color
        self.master.resizable(width=True, height=True) #allows resizing
        self.master.geometry("{}x{}".format(700,400)) #sets the starting size of the window

        self.varFName = StringVar()
        self.varLName = StringVar()

        print(self.varFName.get()) #using .get() will print the value stored rather than the object name
        print(self.varLName.get()) #prints into the console only
        #the self. is important!!

        #the labels for the entry boxes and where they are on the grid-- syntax: Label([where it's placed], [what it says], [formatting])
        self.lblFName = Label(self.master,text='First Name: ', font=("helvetica", 16), fg='black', bg='darkgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0)) #sets up a grid layout with column placement and padding

        self.lblLName = Label(self.master,text='Last Name: ', font=("helvetica", 16), fg='black', bg='darkgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        # the display of the text entered by the user
        self.lblDisplay = Label(self.master,text='', font=("helvetica", 16), fg='black', bg='darkgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        # the entry boxes for the user
        self.txtFName = Entry(self.master,text=self.varFName, font=("helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))
        
        self.txtLName = Entry(self.master,text=self.varLName, font=("helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        #the buttons to submit or cancel. The commands are defined below
        self.btnSubmit = Button(self.master,text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master,text='Cancel', width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    #the functions in the button commands
    def submit(self):
        #assign the value from the first name variable to fn
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

        
    def cancel(self):
        self.master.destroy()
        


if __name__ == "__main__":
    root = Tk() #store the native Tkinter functionaliy in the variable 'root'
    App = ParentWindow(root) #instantiate the ParentWindow class with the arguement 'root' and store it in "App"
    root.mainloop() #this keeps the app running until the user closes it



    
