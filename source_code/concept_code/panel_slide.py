import customtkinter
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
        

class PanelSwitch(customtkinter.CTk):

    def __init__(self):

        customtkinter.CTk.__init__(self)
        self.geometry('900x666')
        self.title('Panel Switch')

        whiteframe = customtkinter.CTkFrame(self, fg_color='white',width=900, height=666)
        whiteframe.place(x = 0, y = 0)

        button = customtkinter.CTkButton(whiteframe, fg_color='pink', text = 'Sign Up', width = 40, height = 30, command = self.signup)
        button.place(x = 0, y = 0)

    def signup(self):

        signup = SignUp(self)
        slideUp(self, signup)

class FrameLeave(customtkinter.CTkButton):

    def __init__(self, master,width, height,corner_radius, border_width, bg_color, fg_color,hover_color, text_color,text):

        self.master = master
        customtkinter.CTkButton.__init__(self, master = master,
                                width = width,
                                height = height,
                                corner_radius = corner_radius,
                                border_width = border_width,
                                bg_color = bg_color,
                                fg_color = fg_color, 
                                hover_color = hover_color,
                                text_color = text_color,
                                text = text,
                                command = self.press_destroy)
        
    def press_destroy(self):

        self.master.destroy()


class SignUp(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master,width = 900, height = 666, fg_color='pink')
        FrameLeave(self, 20,20,1,1,'black','black','blue','white','Close').place(x = 0, y = 0)
        

def main():

    HDP = PanelSwitch()
    HDP.mainloop()

if __name__ == '__main__':
    main()