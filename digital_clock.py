import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar


mainwindow = tk.Tk()
mainwindow.title("Digital Calendar")

date_time_str = StringVar()

current_time = datetime.now()
day = current_time.strftime("%d")
month = current_time.strftime("%m")
year = current_time.strftime("%Y")

def update_date_time():
    day = datetime.today().strftime("%A")
    month = datetime.today().strftime("%B")
    year = datetime.today().strftime("%G")
    time = datetime.today().strftime("%X")
    date = datetime.today().strftime("%d")

    date_time_full_str = month + " " + date + " " + year + "\n" + day + " " + time
    date_time_str.set(date_time_full_str)

    date_time_label.after(1000, update_date_time)

date_time_label = Label(mainwindow, textvariable=date_time_str,
                        width="60",
                        height="3",
                        bg="black",
                        fg="white",
                        font=("Gabriola", 40))

date_time_label.pack(anchor="center")

cal = Calendar(mainwindow, selectmode="day", year=int(year), month=int(month), day=int(day))
cal.pack()


update_date_time()

mainwindow.geometry("800x580")
mainwindow.resizable(False, False)
mainwindow.mainloop()