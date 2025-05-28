import tkinter as tk
from tkinter import StringVar, Button, Entry



mainwindow = tk.Tk()
mainwindow.title('Calculator')

ans_entry = Entry(mainwindow, relief="raised", bd=5, width=20, font=('Arial', 15), bg="green", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

btn_1 = Button(mainwindow, text="1", padx=20, pady=10)
btn_1.grid(row=1, column=0)

btn_2 = Button(mainwindow, text="2", padx=20, pady=10)
btn_2.grid(row=1, column=1)

btn_3 = Button(mainwindow, text="3", padx=20, pady=10)
btn_3.grid(row=1, column=2)

btn_div = Button(mainwindow, text="/", padx=20, pady=10)
btn_div.grid(row=1, column=3)

btn_4 = Button(mainwindow, text="4", padx=20, pady=10)
btn_4.grid(row=2, column=0)

btn_5 = Button(mainwindow, text="5", padx=20, pady=10)
btn_5.grid(row=2, column=1)

btn_6 = Button(mainwindow, text="6", padx=20, pady=10)
btn_6.grid(row=2, column=2)

btn_mul = Button(mainwindow, text="*", padx=20, pady=10)
btn_mul.grid(row=2, column=3)

btn_7 = Button(mainwindow, text="7", padx=20, pady=10)
btn_7.grid(row=3, column=0)

btn_8 = Button(mainwindow, text="8", padx=20, pady=10)
btn_8.grid(row=3, column=1)

btn_9 = Button(mainwindow, text="9", padx=20, pady=10)
btn_9.grid(row=3, column=2)

btn_sub = Button(mainwindow, text="-", padx=20, pady=10)
btn_sub.grid(row=3, column=3)

btn_clear = Button(mainwindow, text="C", padx=20, pady=10)
btn_clear.grid(row=4, column=0)

btn_0 = Button(mainwindow, text="0", padx=20, pady=10)
btn_0.grid(row=4, column=1)

btn_ans = Button(mainwindow, text="=", padx=20, pady=10)
btn_ans.grid(row=4, column=2)

btn_plus = Button(mainwindow, text="+", padx=20, pady=10)
btn_plus.grid(row=4, column=3)

btn_oct = Button(mainwindow, text="O", padx=20, pady=10)
btn_oct.grid(row=5, column=0)

btn_hex = Button(mainwindow, text="H", padx=20, pady=10)
btn_hex.grid(row=5, column=1)

btn_dot = Button(mainwindow, text=".", padx=20, pady=10)
btn_dot.grid(row=5, column=2)

btn_plus = Button(mainwindow, text="+", padx=20, pady=10)
btn_plus.grid(row=5, column=3)





#mainwindow.geometry("300x300")
mainwindow.resizable(False, False)
mainwindow.mainloop()