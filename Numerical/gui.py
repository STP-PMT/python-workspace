from tkinter import *
from tkinter.font import *

root = Tk()
root.geometry("560x410")
l=Label(text='Show image',font='none 20',width=35,anchor=CENTER).place(x=10,y=5)
catBT = Button(text ='Cat',width = 15,anchor=CENTER)
dogtBT = Button(text ='Dog',width = 15,anchor=CENTER)
pigBT = Button(text ='Pig',width = 15,anchor=CENTER)
clearBT = Button(text ='Clear',width = 15,anchor=CENTER)
outputLabel = Label(width=76,height=20,borderwidth=2,relief='groove')

catBT.place(x=10,y=50)
dogtBT.place(x=150,y=50)
pigBT.place(x=290,y=50)
clearBT.place(x=430,y=50)
outputLabel.place(x=10,y=90)

root.mainloop()
