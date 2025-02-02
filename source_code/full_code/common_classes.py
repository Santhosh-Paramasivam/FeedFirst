import customtkinter
from PIL import Image

### COLOUR CONSTANTS ####################

darkPurple = '#0C1765'
lightPurple = '#505FC8'
lightPink = '#FFF5F9'

class Error(customtkinter.CTkToplevel):

    def __init__(self, master, errors):

        customtkinter.CTkToplevel.__init__(self)
        self.geometry('500x500')
        self.title('Error')
        self.transient(master=master)

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Error\Error.png'),
                                                  dark_image=Image.open(r'images\Error\Error.png'),
                                                  size=(500, 500))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

        errorFrame = customtkinter.CTkScrollableFrame(self, width = 390, height = 310, bg_color='white',fg_color='white')
        errorFrame.place(x = 50, y = 100)

        # 190 442

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Exit', hover_color=lightPurple)
        exitButton.place(x = 190, y = 445)

        i = 0
        for error in errors: 
            customtkinter.CTkLabel(errorFrame, width = 390, height = 38, fg_color='white', text = error, anchor='center').grid(column = 0, row = i)
            i+=1

class FrameLeave(customtkinter.CTkButton):

    def __init__(self, master, width, height, corner_radius, border_width, bg_color, fg_color, hover_color, text_color, text):

        self.master = master
        customtkinter.CTkButton.__init__(self, master=master,
                                         width=width,
                                         height=height,
                                         corner_radius=corner_radius,
                                         border_width=border_width,
                                         bg_color=bg_color,
                                         fg_color=fg_color,
                                         hover_color=hover_color,
                                         text_color=text_color,
                                         text=text,
                                         command=self.press_destroy)

    def press_destroy(self):
        self.master.destroy()
