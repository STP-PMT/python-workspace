from tkinter import *
from PIL import ImageTk,Image
import random

def showImage():
    img = Image.open("data/Image/dog.jpg")
    img_resize = img.resize((400,320), Image.ANTIALIAS)
    file_img = ImageTk.PhotoImage(img_resize)
    canvas.create_image(0,0,anchor=NW,image=file_img)
    canvas.image =file_img 
def clearImage():
    canvas.delete('all')

root = Tk()
root.geometry("425x375")
showButton = Button(text = 'Show',width =10,anchor=CENTER,command=showImage)
clearButton = Button(text = 'Clear',width =10,anchor=CENTER,command=clearImage)
canvas = Canvas(width=400,height=320,borderwidth=2,relief='groove')

showButton.place(x=120,y=8)
clearButton.place(x=220,y=8)
canvas.place(x=8,y=40)
root.mainloop()