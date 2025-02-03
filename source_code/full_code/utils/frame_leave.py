import customtkinter
from PIL import Image

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
