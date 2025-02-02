import tkinter as tk
import customtkinter
import math

def widget_move(root,widget,x_org,y_org):
    button_frame = tk.Frame(root)
    button_frame.pack()
    global speed
    global coordinates
    speed_entry = tk.Entry(button_frame, width =17, font = ('Arial',13))
    speed_entry.insert(0, '5')
    speed_entry.grid(row = 0, column = 0, columnspan = 3)
    global x
    global y
    x = x_org
    y = y_org
    def move(direction):
        global speed
        global coordinates
        global x
        global y
        speed = int(speed_entry.get())
        if direction == 'left':
            x-=speed
        if direction == 'right':
            x+=speed
        if direction == 'up':
            y-=speed
        if direction == 'down':
            y+=speed
        coordinates.destroy()
        coordinates = tk.Label(button_frame, text = str(x)+','+str(y), font = ('Arial',13))
        coordinates.grid(row = 3, column = 0, columnspan = 3)
        widget.place(x = x, y = y)

        return
    button_left = tk.Button(button_frame, text = '<', padx=18, pady = 36,command=lambda: move('left'))
    button_right = tk.Button(button_frame, text = '>', padx=18, pady = 36,command=lambda: move('right'))
    button_up = tk.Button(button_frame, text = '^', padx=16, pady = 12,command=lambda: move('up'))
    button_down = tk.Button(button_frame, text = 'v', padx=16, pady = 12,command=lambda: move('down'))
    coordinates = tk.Label(button_frame)
    button_left.grid(row = 1, column = 0, rowspan = 2)
    button_right.grid(row = 1, column = 2, rowspan = 2)
    button_up.grid(row = 1, column = 1)
    button_down.grid(row = 2, column = 1)
    return

def lengthen_widget_downwards(root,widget, init_height, final_height,speed,ms = 10):

    height = init_height

    lengthen_widget_child(root,widget,height,speed,final_height,ms)


def lengthen_widget_child(root,widget, height, speed, final_height, ms = 10):

    if(height <= final_height):

        change = speed * (math.sqrt(math.pow(math.sin(height/final_height * math.pi),2)))
        height+=change
        widget.configure(height=height)
        root.after(ms, lambda : lengthen_widget_child(root,widget,height, speed, final_height,ms))