import customtkinter
from PIL import Image

from .frame_leave import FrameLeave

import constants.colour_constants as cc

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

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 190, y = 445)

        i = 0
        for error in errors: 
            customtkinter.CTkLabel(errorFrame, width = 390, height = 38, fg_color='white', text = error, anchor='center').grid(column = 0, row = i)
            i+=1
