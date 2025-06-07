from tkinter import StringVar, Button, Label, filedialog, PhotoImage, Menu, Scale, Listbox
import tkinter as tk

mainwindow = tk.Tk()
mainwindow.title("Audio Player")

progress_played_str = StringVar()
volume_str = StringVar()

mn = Menu(mainwindow)
mainwindow.config(menu=mn)


fileMn = Menu(mn, tearoff=0)
mn.add_cascade(label="Open file", menu=fileMn)

fileMn.add_command(label="Select file/files")


controlsMusicMenu = Menu(mn, tearoff=0)
mn.add_cascade(label="Control Music", menu=controlsMusicMenu)

controlsMusicMenu.add_command(label="Play")
controlsMusicMenu.add_command(label="Pause/Resume")
controlsMusicMenu.add_command(label="Stop")

TrackDataMenu = Menu(mn, tearoff=0)
mn.add_cascade(label="Other", menu=TrackDataMenu)

controlsMusicMenu.add_command(label="Track Info")
controlsMusicMenu.add_command(label="Pattern_1")
controlsMusicMenu.add_command(label="Pattern_2")
controlsMusicMenu.add_command(label="Pattern_3")
controlsMusicMenu.add_command(label="Pattern_4")


musicFileList = Listbox(mainwindow)
musicFileList.config(height=18, width=52)
musicFileList.grid(column=0, row=0, columnspan=6)


animationLabelRight = Label(mainwindow, justify="left")
animationLabelRight.grid(column=5, row=0, columnspan=5)


trackProgressScale = Scale(mainwindow, orient='horizontal', from_=0, to=100)
trackProgressScale.config(length=520, showvalue=0)
trackProgressScale.grid(column=0, row=1, columnspan=9)

duration_label = Label(mainwindow, textvariable=progress_played_str)
duration_label.config(fg="black", bd=0.5, relief="sunken", width=19)
duration_label.grid(column=9, row=1)

progress_played_str.set("00:00:00/00:00:00")

filesphoto = PhotoImage(file="../../images/files.png")
filesButton = Button(mainwindow, text="Files", image=filesphoto, compound="top")
filesButton.grid(column=0, row=2)

playphoto = PhotoImage(file="../../images/play.png")
playButton = Button(mainwindow, text="Play", image=playphoto, compound="top")
playButton.grid(column=1, row=2)

pausephoto = PhotoImage(file="../../images/pause.png")
pauseButton = Button(mainwindow, text="Pause", image=pausephoto, compound="top")
pauseButton.grid(column=2, row=2)

stopphoto = PhotoImage(file="../../images/stop.png")
stopButton = Button(mainwindow, text="Stop", image=stopphoto, compound="top")
stopButton.grid(column=3, row=2)

prevphoto = PhotoImage(file="../../images/previous.png")
prevButton = Button(mainwindow, text="Previous", image=prevphoto, compound="top")
prevButton.grid(column=4, row=2)

nextphoto = PhotoImage(file="../../images/next.png")
nextButton = Button(mainwindow, text="Next", image=nextphoto, compound="top")
nextButton.grid(column=5, row=2)

mutephoto = PhotoImage(file="../../images/mute.png")
muteButton = Button(mainwindow, text="Mute", image=mutephoto, compound="top")
muteButton.grid(column=6, row=2)

volMinusphoto = PhotoImage(file="../../images/volume_minus.png")
volMinusButton = Button(mainwindow, text="Vol +", image=volMinusphoto, compound="top")
volMinusButton.grid(column=7, row=2)

volPlusphoto = PhotoImage(file="../../images/volume_plus.png")
volPlusButton = Button(mainwindow, text="Vol -", image=volPlusphoto, compound="top")
volPlusButton.grid(column=8, row=2)

volume_str.set("20")
volume_label = Label(mainwindow, textvariable=volume_str)
volume_label.config(fg="white", bg="black", justify="center", width="5", font=("Impact", 40))
volume_label.grid(column=9, row=2)

volume_scale = Scale(mainwindow, orient="vertical", from_=10, to=0, length=396, showvalue=0)
volume_scale.grid(column=10, row=0, rowspan=3)


mainwindow.resizable(width=False, height=False)
mainwindow.geometry("684x400")
mainwindow.mainloop()