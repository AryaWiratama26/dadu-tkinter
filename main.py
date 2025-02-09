import random
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def dadu():
    return random.randint(1,6)


sc_dadu = tk.Tk()
sc_dadu.geometry("600x600")

# Bg image
image_dadu = Image.open("./images/dadu.jpg")
background_img = ImageTk.PhotoImage(image_dadu)

bg_label = tk.Label(sc_dadu, image=background_img)
bg_label.place(relheight=1, relwidth=1)


sc_dadu.mainloop()