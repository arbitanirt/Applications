from tkinter import Label, Button, StringVar, filedialog, Entry, PhotoImage
import tkinter as tk


mainwindow = tk.Tk()
mainwindow.title('Image Exporter')


open_btn = Button(mainwindow, text="Open", pady=2 , padx=25, font=('Arial', 12))
open_btn.place(x=10, y=10)

width_label = Label(mainwindow, text="Width", font=('Arial', 14))
width_label.place(x=120, y=12)

width_entry_str = StringVar()
width_entry = Entry(mainwindow, textvariable=width_entry_str, relief="raised", bd=2, font=('Arial', 12))
width_entry.place(x=190, y=10, height=34)

height_label = Label(mainwindow, text="Height", font=('Arial', 14))
height_label.place(x=385, y=12)

height_entry_str = StringVar()
height_entry = Entry(mainwindow, textvariable=height_entry_str, relief="raised", bd=2, font=('Arial', 12))
height_entry.place(x=460, y=10, height=34)


resize_btn = Button(mainwindow, text="Resize", pady=2, padx=25, font=('Arial', 12))
resize_btn.place(x=665, y=10)

save_btn = Button(mainwindow, text="Save", pady=2, padx=25, font=('Arial', 12))
save_btn.place(x=780, y=10)

mainwindow.geometry('890x600')
mainwindow.resizable(False, False)
mainwindow.mainloop()