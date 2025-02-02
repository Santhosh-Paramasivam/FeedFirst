import customtkinter
import math

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
        signup.place(x = 0, y = 0)

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