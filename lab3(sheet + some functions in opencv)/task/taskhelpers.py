# Note: this is not a complete code don't expect it to work like this.


from tkinter import Tk, Label, Radiobutton, StringVar
from PIL import Image, ImageTk
import cv2



# render an opencv image on a tkinter label
def convertImageToTkinter(self):
        b,g,r = cv2.split(self.img)
        img = cv2.merge((r,g,b))
        im = Image.fromarray(img)
        im = im.resize((500,500))
        imgtk = ImageTk.PhotoImage(image=im)
        label = Label(self.master, image=imgtk)


# Creating the radio button
var = StringVar(root) # this a variable to check which radio button was clicked if you have multiple radio buttons
def selected():
    print(var.get())
Radiobutton(root, text="your text", variable=var, value= 0 ,command= selected)

