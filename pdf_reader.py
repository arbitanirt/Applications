from tkinter import Button, filedialog
import tkinter as tk
from tkPDFViewer import tkPDFViewer


mainwindow = tk.Tk()
mainwindow.title("PDF READER")

def open_handler():
    filename = filedialog.askopenfilename(initialdir=".", filetypes=(("PDF files", "*.pdf"),))

    if filename:
        #print("Opening file: " + filename)
        show_obj = tkPDFViewer.ShowPdf()
        show_obj.img_object_li.clear()
        pdf_view = show_obj.pdf_view(mainwindow, pdf_location=filename)
        pdf_view.place(x=30, y=60, width=985, height=520)


openButton = Button(mainwindow, text="Select PDF File", width=20, height=2, command=open_handler)
openButton.place(x=8, y=8)







mainwindow.geometry("1200x600")
mainwindow.resizable(False, False)
mainwindow.mainloop()