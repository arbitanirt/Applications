from tkinter import Scale, Label, StringVar
import tkinter as tk


mainwindow = tk.Tk()
mainwindow.title("Color Picker")

def get_str_from_num(value):
    color_data = {}

    color_value = str(hex(int(value))).split('x')[1]
    if len(color_value) < 2:
        color_value = "0" + color_value

    percentage_value_str = "0 %"
    color_percentage_value = int(value)
    if(color_percentage_value > 0):
        color_percentage_value = str(int(float(color_percentage_value * 100)/255))

        if (len(color_percentage_value) < 2):
            color_percentage_value = "0" + color_percentage_value
        percentage_value_str = color_percentage_value + " %"


    color_data['hex'] = color_value.upper()
    color_data['percentage'] = percentage_value_str
    return color_data

def get_hex_color_values():
    color_info_dict = {}

    red_value = get_str_from_num(scroller_red.get())
    green_value = get_str_from_num(scroller_green.get())
    blue_value = get_str_from_num(scroller_blue.get())

    color_info_dict['red_hex'] = red_value['hex']
    color_info_dict['red_percentage'] = red_value['percentage']

    color_info_dict['green_hex'] = green_value['hex']
    color_info_dict['green_percentage'] = green_value['percentage']

    color_info_dict['blue_hex'] = blue_value['hex']
    color_info_dict['blue_percentage'] = blue_value['percentage']


    return color_info_dict

def update_values():
    color_values = get_hex_color_values()

    color_hex_value = "#" + color_values['red_hex'] + color_values['green_hex'] + color_values['blue_hex']
    color_hex_code.set(color_hex_value)
    result_label.config(bg=color_hex_value)

    red_percentage_value.set(color_values['red_percentage'])
    green_percentage_value.set(color_values['green_percentage'])
    blue_percentage_value.set(color_values['blue_percentage'])

    #red_value = get_str_from_num(scroller_red.get())
    #green_value = get_str_from_num(scroller_green.get())
    #blue_value = get_str_from_num(scroller_blue.get())

    #print("RED : ", red_value, " GREEN : ", green_value, " BLUE : ", blue_value)


##### function

def red_scale_handler(value):
    update_values()

def green_scale_handler(value):
    update_values()

def blue_scale_handler(value):
    update_values()

color_hex_code = StringVar()
color_hex_code.set('#000')

result_label = Label(mainwindow, padx=5, pady=5, textvariable=color_hex_code, fg="white", font=("Arial", 43))
result_label.config(bg=color_hex_code.get())
result_label.place(x=5, y=5, width=490, height=280)

##### RED

scroller_red = Scale(mainwindow, from_=0, to=255)
scroller_red.config(length=447, orient='horizontal', troughcolor="red", fg='red', command=red_scale_handler)
scroller_red.set(0)
scroller_red.place(x=0, y=300)

red_percentage_value = StringVar()
red_percentage_label = Label(mainwindow, textvariable=red_percentage_value, fg="red")
red_percentage_value.set("0 %")
red_percentage_label.place(x=455, y=319)


##### GREEN

scroller_green = Scale(mainwindow, from_=0, to=255)
scroller_green.config(length=447, orient='horizontal', troughcolor="green", fg='green', command=green_scale_handler)
scroller_green.set(0)
scroller_green.place(x=0, y=350)

green_percentage_value = StringVar()
green_percentage_label = Label(mainwindow, textvariable=green_percentage_value, fg="green")
green_percentage_value.set("0 %")
green_percentage_label.place(x=455, y=369)


##### BLUE

scroller_blue = Scale(mainwindow, from_=0, to=255)
scroller_blue.config(length=447, orient='horizontal', troughcolor="blue", fg='blue', command=blue_scale_handler)
scroller_blue.set(0)
scroller_blue.place(x=0, y=400)

blue_percentage_value = StringVar()
blue_percentage_label = Label(mainwindow, textvariable=blue_percentage_value, fg="blue")
blue_percentage_value.set("0 %")
blue_percentage_label.place(x=455, y=419)




mainwindow.geometry("500x475")
mainwindow.mainloop()