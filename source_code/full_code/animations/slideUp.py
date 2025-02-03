import math

def slideUp(master, widget):

    window_height = 675
    end_x = 0
    end_y = 0
    speed = 27
    ms = 10
    y = end_y + window_height
    end_y = end_y + 1

    slideUpChild(master, widget, window_height, end_x, y, speed, end_y, ms)


def slideUpChild(master, widget, window_height, end_x, y, speed, end_y, ms = 10):

    if(int(y - 1) > int(end_y)):
        change = speed * math.sin(((y - end_y)/(window_height)) * math.pi)
        y-= change
        widget.place(x = end_x, y = y)
        master.after(ms, lambda : slideUpChild(master, widget, window_height, end_x, y, speed, end_y, ms))

    else:
        widget.place(x = end_x, y = end_y - 1)

