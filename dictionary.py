from tkinter import Button, Entry, Label, StringVar
import tkinter as tk
from urllib.request import urlopen
from bs4 import BeautifulSoup


mainwindow = tk.Tk()
mainwindow.title("Dictionary")

word_info = StringVar()

data_dict = {}

def get_dict_data_from_webUrl():
    global data_dict

    url="https://ielts.com.au/australia/prepare/article-100-new-english-words-and-phrases-updated-2020"

    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    dict_val = soup.find_all("div", {"class": "article-wrapper"})
    dict_val = dict_val[0]
    dict_val = dict_val.find_all('td')

    list_words = [dict_val[word].get_text().lower().strip() for word in range(0, len(dict_val), 2)]
    list_def = [dict_val[word_def].get_text() for word_def in range(1, len(dict_val), 2)]


    for word in range(len(list_words)):
        data_dict[list_words[word]] = list_def[word]

    print(data_dict)


get_dict_data_from_webUrl()

def search_handler():
    global data_dict
    typed_word = input_entry.get().lower().strip()

    #typed_word = input_entry.get()
    if typed_word in data_dict.keys():
        word_info.set(data_dict[typed_word])
    else:
        word_info.set(typed_word + " is not found in the dictionary.")


def add_handler():
    global data_dict
    word_info.set(" ")
    word = word_entry.get()
    word_def = word_def_entry.get()

    if word != "" and word_def != "":
        data_dict[word] = word_def
        word_info.set("New word " + word + " is added.")
        word_entry_str.set(" ")
        word_def_str.set(" ")

input_entry = Entry(mainwindow, relief="raised", bd=2, font=('Arial', 15), width=55)
input_entry.place(x=10, y=10)

search_btn = Button(mainwindow, text='Search', pady=2, padx=20, command=search_handler)
search_btn.place(x=630, y=10)

word_label = Label(mainwindow, text='Word :', font=('Arial', 14))
word_label.place(x=10, y=50)

word_entry_str = StringVar()

word_entry = Entry(mainwindow, relief="raised", bd=2, font=('Arial', 15), textvariable=word_entry_str)
word_entry.place(x=80, y=50)

word_def_label = Label(mainwindow, text='Define :', font=('Arial', 14))
word_def_label.place(x=320, y=50)

word_def_str = StringVar()
word_def_entry = Entry(mainwindow, relief="raised", bd=2, font=('Arial', 15), textvariable=word_def_str)
word_def_entry.place(x=395, y=50)

add_btn = Button(mainwindow, text='Add', pady=2, padx=27, command=add_handler)
add_btn.place(x=630, y=50)

info_label = Label(mainwindow, textvariable=word_info ,font=('Arial', 16), relief="raised", bd=2, width=58, height=5, wraplength=500)
info_label.place(x=10, y=90)

mainwindow.resizable(False, False)
mainwindow.geometry("730x255")
mainwindow.mainloop()