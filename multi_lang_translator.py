from tkinter import StringVar, ttk, Label, Button, Entry
import tkinter as tk
from translate import Translator

mainwindow = tk.Tk()
mainwindow.title('Multi Language Translator')

def translate_handler():
    lang = selected_lang.get()
    input_str = input_entry.get()

    translator = Translator(to_lang=lang)
    output_str.set(translator.translate(input_str))

    #print(input_str, lang)

info_label = Label(mainwindow, text='Enter message here : ', pady=15)
info_label.pack()

input_entry = Entry(mainwindow, relief="raised", bd=2, font= ('Arial', 15))
input_entry.pack(fill='x', padx=15, pady=10)

selected_lang = StringVar()
lang_cb = ttk.Combobox(mainwindow, textvariable=selected_lang)
lang_cb['state'] = 'readonly'
Languages = ['Hindi', 'German', 'Spanish', 'Chinese']
lang_cb['values'] = [m for m in Languages]
lang_cb.set('Français')
lang_cb.pack()

translate_btn = Button(mainwindow, text="translate", padx=43, pady=10, command=translate_handler)
translate_btn.pack(pady=10)

output_str = StringVar()
output_label = Label(mainwindow, textvariable=output_str)
output_label.config(relief='raised', bd=2, height=6, font=('Arial', 24))
output_label.pack(fill='x', padx=20, pady=10)



mainwindow.geometry('800x450')
mainwindow.resizable(False, False)
mainwindow.mainloop()
