from tkinter import StringVar, ttk, Label, Button, Entry
import tkinter as tk


mainwindow = tk.Tk()
mainwindow.title('Multi Language Translator')

info_label = Label(mainwindow, text='Enter message here : ', pady=15)
info_label.pack()

input_entry = Entry(mainwindow, relief="raised", bd=2, font= ('Arial', 15))
input_entry.pack(fill='x', padx=15, pady=10)

selected_lang = StringVar()
lang_cb = ttk.Combobox(mainwindow, textvariable=selected_lang)
lang_cb['state'] = 'readonly'
Languages = ['Français', 'Arabe', 'Anglais', 'Espagne']
lang_cb['values'] = [m for m in Languages]
lang_cb.set('Français')
lang_cb.pack()

translate_btn = Button(mainwindow, text="translate", padx=43, pady=10)
translate_btn.pack(pady=10)

output_str = StringVar()
output_label = Label(mainwindow, textvariable=output_str)
output_label.config(relief='raised', bd=2, height=6, font=('Arial', 24))
output_label.pack(fill='x', padx=20, pady=10)



mainwindow.geometry('800x450')
mainwindow.resizable(False, False)
mainwindow.mainloop()