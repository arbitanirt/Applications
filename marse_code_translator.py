import tkinter as tk
from tkinter import Button, Label, Entry, PhotoImage, StringVar, Toplevel


mainwindow = tk.Tk()
mainwindow.title('Marse Code Translator')

info_label = Label(mainwindow, text="Enter message here:")
info_label.pack()
info_label.config(pady=15)


input_entry = Entry(mainwindow, relief="raised", bd=2, font=("Arial", 20))
input_entry.pack(fill="x", padx=50, pady=10)

generate_marse_code_from_str_btn = Button(mainwindow, text="String to marse Code")
generate_marse_code_from_str_btn.config(pady=10, padx=10)
generate_marse_code_from_str_btn.pack()


generate_str_from_marse_code_btn = Button(mainwindow, text="marse Code to String")
generate_str_from_marse_code_btn.config(pady=10, padx=10)
generate_str_from_marse_code_btn.pack()

output_label = Label(mainwindow)
output_label.pack(fill="x", padx=20, pady=10)
output_label.config(relief="raised", bd=2, height=3, font=("Arial", 24))


marse_code_ref_button = Button(mainwindow, text="Marse Codes")
marse_code_ref_button.config(pady=10, padx=10)
marse_code_ref_button.pack()


mainwindow.geometry('800x500')
mainwindow.resizable(False, False)
mainwindow.mainloop()