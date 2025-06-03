from tkinter import ttk, StringVar
import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime




mainwindow = tk.Tk()
mainwindow.title("Sensex/Nifty Live Stock Market Update")

def get_nifty_data_from_weburl():
    nifty_url = "https://www.moneycontrol.com/indian-indices/nifty-50-9.html"
    page = urlopen(nifty_url)
    soup = BeautifulSoup(page, "html.parser")
    nifty_val = soup.find_all("div", {"class": "stickymcont"})
    nifty_val = nifty_val[0]
    nifty_val = nifty_val.find_all("div")[1]
    nifty_val = nifty_val.get_text()
    return nifty_val
    #print(nifty_val, type(nifty_val))



def get_sensex_data_from_weburl():
    sensex_url = "https://www.moneycontrol.com/indian-indices/sensex-4.html"
    page = urlopen(sensex_url)
    soup = BeautifulSoup(page, "html.parser")
    sensex_val = soup.find_all("div", {"class": "stickymcont"})
    sensex_val = sensex_val[0]
    sensex_val = sensex_val.find_all("div")[1]
    sensex_val = sensex_val.get_text()
    return sensex_val


def get_sensex_nifty_data():
    data_list = []

    nifty_val = get_nifty_data_from_weburl()
    sensex_val = get_sensex_data_from_weburl()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    data_list.append(nifty_val)
    data_list.append(current_time)
    data_list.append(sensex_val)
    data_list.append(current_time)

    return data_list


#print(data)




columns = ("Nifty", "Nifty_Time", "Sensex", "Sensex_Time")
tree = ttk.Treeview(mainwindow, columns=columns, show="headings")
tree.heading("Nifty", text="Nifty")
tree.heading("Nifty_Time", text="Nifty_Time")
tree.heading("Sensex", text="Sensex")
tree.heading("Sensex_Time", text="Sensex_Time")
tree.place(x=10, y=10)

current_sensex_data = "0"
current_nifty_data = "0"

def add_data_to_table():
    global current_sensex_data, current_nifty_data
    data = get_sensex_nifty_data()

    nifty_val = data[0]
    sensex_val = data[2]
    mainwindow.title("Data Updated at : " + str(data[1]))

    if not(nifty_val == current_nifty_data and sensex_val == current_sensex_data):
        current_nifty_data = nifty_val
        current_sensex_data = sensex_val

        tree.insert('', tk.END, values=data)
        for column in tree['columns']:
            tree.column(column, anchor="center")

    mainwindow.after(5000, add_data_to_table)


add_data_to_table()

mainwindow.geometry("825x255")
mainwindow.resizable(False, False)
mainwindow.mainloop()
