from tkinter import Button, Label, Entry, PhotoImage
import tkinter as tk


mainwindow = tk.Tk()
mainwindow.title("QR Code Generator")

info_label = Label(mainwindow, text="Enter message here to generate QR Code", pady=15)
info_label.pack()


input_entry = Entry(mainwindow, relief="raised", bd=2, font=("Arial", 15))
input_entry.pack(fill="x", padx=50, pady=10)


generate_btn = Button(mainwindow, text="Generate QR Code", padx=10, pady=10)
generate_btn.pack()


qr_code_label = Label(mainwindow, bg="blue")
qr_code_label.place(x=300, y=160, width=200, height=200)


mainwindow.geometry("800x380")
mainwindow.resizable(False, False)
mainwindow.mainloop()