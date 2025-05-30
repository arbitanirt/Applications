import tkinter as tk
from tkinter import StringVar, Button, Label, Entry, Place

mainwindow = tk.Tk()
mainwindow.title("Task Check list")

task_label = Label(mainwindow, text="Add a Task", font=("Arial", 12))
task_label.place(x=10, y=10, height=25)

task_str = StringVar()

task_entry = Entry(mainwindow, textvariable=task_str)
task_entry.place(x=100, y=10, height=25, width=200)

add_item_btn = Button(mainwindow, text="Add Task", pady=6, padx=20)
add_item_btn.place(x=10, y=50, width=140)

delete_item_btn = Button(mainwindow, text="Delete", pady=6, padx=20)
delete_item_btn.place(x=160, y=50, width=140)

save_item_btn = Button(mainwindow, text="Save", pady=6, padx=20)
save_item_btn.place(x=10, y=340, width=290)


mainwindow.geometry("325x390")
mainwindow.resizable(False, False)
mainwindow.mainloop()