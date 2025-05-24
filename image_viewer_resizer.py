from tkinter import Label, Button, StringVar, filedialog, Entry, PhotoImage
import tkinter as tk
from PIL import Image


mainwindow = tk.Tk()
mainwindow.title('Image Exporter')

image_fp = None
data_image = None
photo_image = None

def open_handler():
    global image_fp, data_image

    image_fp = filedialog.askopenfilename(initialdir=".", filetypes=(("PNG Files", "*.png"),))

    if image_fp:
        data_image = PhotoImage(file=image_fp)
        image_label.config(image=data_image)


def width_modified(event):
    global image_fp

    if image_fp:
        w = width_entry.get()
        if w != " " and w.isdigit():
            w = int(w)


            image = Image.open(image_fp)
            image_width = image.width
            image_height = image.height

            width_percentage = int((w*100)/image_width)
            height_set_to = int(image_height * (width_percentage/100))
            height_entry_str.set(str(height_set_to))



def height_modified(event):
    global image_fp

    if image_fp:
        h = height_entry.get()
        if h != " " and h.isdigit():
            h = int(h)

            image = Image.open(image_fp)
            image_width = image.width
            image_height = image.height

            height_percentage = int((h * 100) / image_height)
            width_set_to = int(image_width * (height_percentage / 100))
            width_entry_str.set(str(width_set_to))


def resize_handler():
    global image_fp, photo_image
    if image_fp:
        w = width_entry_str.get()
        h = height_entry_str.get()

        if w != " " and w.isdigit() and h != " " and h.isdigit():
            w = int(w)
            h = int(h)
            image = Image.open(image_fp)
            image.thumbnail((w, h), Image.Resampling.LANCZOS)
            image.save("Sample.png")
            photo_image = PhotoImage(file="Sample.png")
            image_label.config(image=photo_image)


def save_handler():
    global image_fp, data_image
    if image_fp:
        image_save_fp = filedialog.asksaveasfile(initialdir=".", filetypes=(("PNG Files", "*.png"),), defaultextension=".png")

        if image_save_fp:
            w = width_entry_str.get()
            h = height_entry_str.get()

            if w != " " and w.isdigit() and h != " " and h.isdigit():
                w = int(w)
                h = int(h)

                image = Image.open(image_fp)
                image.thumbnail((w, h), Image.Resampling.LANCZOS)
                image.save(image_save_fp.name)


open_btn = Button(mainwindow, text="Open", pady=2 , padx=25, font=('Arial', 12), command=open_handler)
open_btn.place(x=10, y=10)

width_label = Label(mainwindow, text="Width", font=('Arial', 14))
width_label.place(x=120, y=12)

width_entry_str = StringVar()
width_entry = Entry(mainwindow, textvariable=width_entry_str, relief="raised", bd=2, font=('Arial', 12))
width_entry.place(x=190, y=10, height=34)
width_entry.bind("<KeyRelease>", width_modified)

height_label = Label(mainwindow, text="Height", font=('Arial', 14))
height_label.place(x=385, y=12)

height_entry_str = StringVar()
height_entry = Entry(mainwindow, textvariable=height_entry_str, relief="raised", bd=2, font=('Arial', 12))
height_entry.place(x=460, y=10, height=34)
height_entry.bind("<KeyRelease>", height_modified)



resize_btn = Button(mainwindow, text="Resize", pady=2, padx=25, font=('Arial', 12), command=resize_handler)
resize_btn.place(x=665, y=10)

save_btn = Button(mainwindow, text="Save", pady=2, padx=25, font=('Arial', 12), command=save_handler)
save_btn.place(x=780, y=10)

image_label = Label(mainwindow)
image_label.config(image="")
image_label.pack(fill="both", padx=10, pady=50)

mainwindow.geometry('890x600')
mainwindow.resizable(False, False)
mainwindow.mainloop()
