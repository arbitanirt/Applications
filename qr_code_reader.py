from tkinter import Button, Label, PhotoImage, filedialog, StringVar
import tkinter as tk
from PIL import Image, ImageTk

qr_file_ptr = None

mainwindow = tk.Tk()
mainwindow.title("QR Code Reader")
mainwindow.config(pady=20)

def select_qr_code_image():
    global qr_file_ptr
    qr_file_ptr = filedialog.askopenfilename(initialdir=".", filetypes=(("PNG Files", "*.png"), ))
    if qr_file_ptr:
        image = Image.open(qr_file_ptr)
        image.thumbnail((200, 200))
        image.save(qr_file_ptr)

        qr_img = PhotoImage(file=qr_file_ptr)
        qr_code_lbl.config(image=qr_img)

def read_qr_code():
    global qr_file_ptr
    import cv2
    img = cv2.imread(qr_file_ptr)
    detector = cv2.QRCodeDetector()
    values = detector.detectAndDecode(img)
    #print(values)
    qr_info_str.set(values[1])

select_btn = Button(mainwindow, text="Select a QR Code Image read", command=select_qr_code_image)
select_btn.config(padx=10, pady=10)
select_btn.pack()

qr_code_lbl = Label(mainwindow)
qr_code_lbl.pack(pady=10)

read_btn = Button(mainwindow, text="Read QR Code", command=read_qr_code)
read_btn.config(padx=10, pady=10)
read_btn.pack()

qr_info_str = StringVar()
output_lbl = Label(mainwindow, textvariable=qr_info_str)
output_lbl.config(relief="raised", bd=2, height=3)
output_lbl.pack(fill="x", padx=20, pady=10)

mainwindow.geometry("800x450")
mainwindow.resizable(False, False)
mainwindow.mainloop()