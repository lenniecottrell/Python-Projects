#import everything from tkinter

from tkinter import *

#open a basic tkinter window
win = Tk()

#create buttons, place them in the window with pack layout
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text="Two")
>>> b1.pack()
>>> b2.pack()
>>> b1.pack(side=LEFT)
>>> b2.pack(side=LEFT)

#add padding with pack layout
>>> b1.pack(side = LEFT, padx = 10)
>>> b2.pack(side = LEFT, padx = 10)
>>> b3 = Button(win, text="Three")
>>> b3.pack(side = BOTTOM)
>>> b4 = Button(win, text="Four")
>>> b4.pack(side = RIGHT)
>>> b4.pack(side = RIGHT, padx = 35)

#open a new window with two buttons, place them using a grid layout
>>> win = Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text="Two")
>>> b1.grid(row=0, column=0)
>>> b2.grid(row=1, column=1)
#add a label to the grid layout
>>> l = Label(win, text="This is a label")
>>> l.grid(row=1, column=0)

#new window with three buttons contained in a frame
>>> win=Tk()
>>> f = Frame(win)
>>> b1 = Button(f, text="One")
>>> b2 = Button(f, text="Two")
>>> b3 = Button(f, text="Three")
>>> b1.pack(side=LEFT)
>>> b2.pack(side=LEFT)
>>> b3.pack(side=LEFT)
>>> l= Label(win, text="This label is over all buttons")
>>> l.pack()
>>> f.pack()

#alter the text of button1
>>> b1.configure(text="Uno")

add functionality to button1
>>> def but1():
	print("Button one was pushed")
>>>b1.configure(command=but1)

#add input for a user using StringVar and Entry methods
>>> v = StringVar()
>>> e = Entry(win, textvariable = v)
>>> e.pack()
>>> v.get()
'This is a test'
>>> v.set("this is set by the program")
>>> win = Tk()
>>> lb = Listbox(win, height=3)
>>> lb.pack()
>>> lb.insert(END, "first entry")
>>> lb.insert(END, "second entry")
>>> lb.insert(END, "third entry")
>>> lb.insert(END, "fourth entry")

#add a scrollbar and connect it to the list
>>> sb = Scrollbar(win, orient=VERTICAL)
>>> sb.pack(side=LEFT, fill=Y)
>>> sb.configure(command=lb.yview)
>>> lb.configure(yscrollcommand=sb.set)

#this will return whatever the cursor has selected in the listbox
>>> lb.curselection()
