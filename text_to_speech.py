from tkinter import Button, IntVar, StringVar, Label, filedialog, ttk, font
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from gtts import gTTS
import os
from playsound import playsound

mainwindow = tk.Tk()
mainwindow.title("Text to Speech")

selected_language = StringVar()
selected_size = IntVar()

selected_language.set("Verdana")
selected_size.set(14)

def open_handler():
    filename = filedialog.askopenfilename(initialdir="./../../", filetypes=(("Text files", "*.txt"),))
    if filename:
        with open(filename, "r") as file:
            textwindow.delete("1.0", "end")
            for line in file:
                textwindow.insert("insert", line)

def save_handler():
    fp = filedialog.asksaveasfile(initialdir="../../", title="Save a file", filetypes=(("Text files", "*.txt"),), defaultextension="*.txt")
    if fp :
        content = textwindow.get("1.0", "end")
        fp.write(content)

openButton = Button(mainwindow, text="Open", width=10, height=2, command=open_handler)
openButton.place(x=8, y=8)

saveButton = Button(mainwindow, text="Save", width=10, height=2, command=save_handler)
saveButton.place(x=90, y=8)

font_Family_label = Label(mainwindow, text="Font")
font_Family_label.place(x=180, y=8)

font_families = font.families()
#for i in font_families:
    #print("font families : ", i)

def value_changed_font(event):
    lang = selected_language.get()
    textwindow.config(font=(lang, selected_size.get()))

font_cb = ttk.Combobox(mainwindow, height=10, textvariable=selected_language)
font_cb.bind("<<ComboboxSelected>>", value_changed_font)
font_cb["values"] = font_families
font_cb["state"] = "readonly"
font_cb.place(x=180, y=28)

font_size_label = Label(mainwindow, text="Font-size")
font_size_label.place(x=350, y=8)

def value_changed_font_size(event):
    font_size = selected_size.get()
    textwindow.config(font=(selected_language.get(), font_size))

font_size_cb = ttk.Combobox(mainwindow, height=10, textvariable=selected_size)
font_cb.bind("<<ComboboxSelected>>", value_changed_font_size)
font_size_cb["values"] = [i for i in range(1, 101)]
font_size_cb["state"] = "readonly"
font_size_cb.place(x=350, y=28)

textwindow = ScrolledText(mainwindow, wrap="word")
textwindow.config(font=(selected_language.get(), selected_size.get()))
textwindow.place(x=8, y=60, width=985, height=520)

def text_to_speech_handler():
    content = textwindow.get("1.0", "end")
    content = content.split("\n")
    #print(content, type(content))
    test_track = "test.mp3"
    if os.path.exists(test_track):
        os.remove(test_track)

    for line in content:
        if len(line):
            obj = gTTS(text=line, lang="en-in", slow=False)
            obj.save(test_track)
            playsound(test_track)

speekButton = Button(mainwindow, text="Text to Speech", width=15, height=2, command=text_to_speech_handler)
speekButton.place(x=510, y=8)

mainwindow.geometry("1000x500")
mainwindow.resizable(False, False)
mainwindow.mainloop()