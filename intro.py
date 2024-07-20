from tkinter import *
from PIL import Image,ImageTk,ImageSequence 
import time
import pygame 
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1000x500")

def gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("1.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

gif()
root.mainloop()