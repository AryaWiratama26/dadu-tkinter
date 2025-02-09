import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.messagebox import showinfo

def dadu():
    get_angka = f"Hasil dadu : {random.randint(1,6)}"
    showinfo(title="Hasil", message=get_angka,)
    

# Buat root screen
sc_dadu = tk.Tk()
sc_dadu.geometry("600x600")
sc_dadu.title("Lempar Dadu")
sc_dadu.resizable(False, False)
sc_dadu.configure(bg="black")

# Bg image
image_dadu = Image.open("./images/dadu.jpg")
background_img = ImageTk.PhotoImage(image_dadu)

# LOad bg image
bg_label = tk.Label(sc_dadu, image=background_img)
bg_label.place(relheight=1, relwidth=1)

# frame utama
main_frame = ttk.Frame(sc_dadu)
main_frame.pack(padx=10,pady=10,fill="x",expand=True)

# label Keterangan
ket_dadu = ttk.Label(main_frame, text="Lempar Dadu Untuk Memulai!",justify='center',anchor='center',font=('Poppins',18))
ket_dadu.pack(padx=10,pady=10,fill="x",expand=True)

# Button dadu
btn_dadu = ttk.Button(main_frame, text="Lempar Sekarang", command=dadu)
btn_dadu.pack(padx=10,pady=10,fill="x",expand=False)

# Loop
sc_dadu.mainloop()