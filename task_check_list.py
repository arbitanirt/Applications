import tkinter as tk
from tkinter import StringVar, Button, Label, Entry
from ttkwidgets import CheckboxTreeview

mainwindow = tk.Tk()
mainwindow.title("Task Check list")

def add_handler():
    task = task_str.get()

    if len(task.strip()):
        tree.insert('', tk.END, text=task)
        task_str.set("")


def delete_handler():
    if len(tree.selection()):
        selected_item = tree.selection()[0]
        tree.delete(selected_item)


def save_handler():
    with open("task_data.txt", "w") as task_file_fp:
        for item in tree.get_children():
            isChecked = tree.tag_has("checked", item)
            isCheckedStr = "checked" if isChecked else "UnChecked"
            data = tree.item(item).get('text')
            data = data + " " + isCheckedStr
            if data[-1] != "\n":
                task_file_fp.write(data + '\n')
            else:
                task_file_fp.write(data)




task_label = Label(mainwindow, text="Add a Task", font=("Arial", 12))
task_label.place(x=10, y=10, height=25)

task_str = StringVar()

task_entry = Entry(mainwindow, textvariable=task_str)
task_entry.place(x=100, y=10, height=25, width=200)

add_item_btn = Button(mainwindow, text="Add Task", pady=6, padx=20, command=add_handler)
add_item_btn.place(x=10, y=50, width=140)

delete_item_btn = Button(mainwindow, text="Delete", pady=6, padx=20, command=delete_handler)
delete_item_btn.place(x=160, y=50, width=140)

save_item_btn = Button(mainwindow, text="Save", pady=6, padx=20, command=save_handler)
save_item_btn.place(x=10, y=340, width=290)

tree = CheckboxTreeview(mainwindow)
tree.place(x=10, y=100, width=290)

task_list = []
with open('task_data.txt', 'r') as task_data_fp:
    for line in task_data_fp.readlines():
        task_list.append(line)


for index, item in enumerate(task_list):
    data = item.split()
    tree.insert('', tk.END, text=data[0])
    if data[1] == 'checked':
        tree._check_ancestor(tree.get_children()[index])


#tree.insert('', tk.END, text="Charge a phone")
#tree._check_ancestor(tree.get_children()[0])


mainwindow.geometry("315x390")
mainwindow.resizable(False, False)
mainwindow.mainloop()