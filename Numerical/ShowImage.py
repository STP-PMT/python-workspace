from tkinter import *
from tkinter.font import *
from PIL import ImageTk,Image
from functools import partial

root = Tk()
root.geometry("560x410")
def showImage(text):
    if(text == 'Cat'):
        img = Image.open("data/Image/cat.png")
    elif(text == 'Dog'):   
        img = Image.open("data/Image/dog.jpg")
    img_resize = img.resize((530,300), Image.ANTIALIAS)
    file_img = ImageTk.PhotoImage(img_resize)
    outputLabel.create_image(0,0,anchor=NW,image=file_img)
    outputLabel.image =file_img 
def clear():
    outputLabel.delete('all')
l=Label(text='Show image',font='none 20',width=35,anchor=CENTER).place(x=10,y=5)
catBT = Button(text ='Cat',width = 15,anchor=CENTER,command=partial(showImage,'Cat'))
dogtBT = Button(text ='Dog',width = 15,anchor=CENTER,command=partial(showImage,'Dog'))
pigBT = Button(text ='Pig',width = 15,anchor=CENTER)
clearBT = Button(text ='Clear',width = 15,anchor=CENTER,command = clear)
outputLabel = Canvas(width=530,height=300,borderwidth=2,relief='groove')

catBT.place(x=10,y=50)
dogtBT.place(x=150,y=50)
pigBT.place(x=290,y=50)
clearBT.place(x=430,y=50)
outputLabel.place(x=10,y=90)

root.mainloop()
