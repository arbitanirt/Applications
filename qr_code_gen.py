from tkinter import Button, Label, Entry, PhotoImage
import tkinter as tk
import qrcode
from PIL import Image

mainwindow = tk.Tk()
mainwindow.title("QR Code Generator")

def generate_qr_code():
    data = input_entry.get()
    img = qrcode.make(data)
    img.save("MyQrCode.png")

    image = Image.open("MyQrCode.png")
    image.thumbnail((200, 200))
    image.save("MyQrCode.png")

    qr_image = PhotoImage(file="MyQrCode.png")
    qr_code_label.config(image=qr_image)

info_label = Label(mainwindow, text="Enter message here to generate QR Code", pady=15)
info_label.pack()

input_entry = Entry(mainwindow, relief="raised", bd=2, font=("Arial", 15))
input_entry.pack(fill="x", padx=50, pady=10)

generate_btn = Button(mainwindow, text="Generate QR Code", padx=10, pady=10, command=generate_qr_code)
generate_btn.pack()

qr_code_label = Label(mainwindow )
qr_code_label.place(x=300, y=160, width=200, height=200)

mainwindow.geometry("800x380")
mainwindow.resizable(False, False)
mainwindow.mainloop()
