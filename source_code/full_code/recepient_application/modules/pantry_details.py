import customtkinter
from PIL import Image
import constants.colour_constants as cc
from database.mysql_connection import mydb, mycursor
from utils.widgets import Error,FrameLeave

class PantryDetails(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)
    
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Recepient\PantryDetailsPage.png'),
                                                  dark_image=Image.open(r'images\Recepient\PantryDetailsPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 385, y = 587)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 775, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 57, y = 180)

        mycursor.execute("SELECT * FROM Pantries")
        pantries = mycursor.fetchall()

        i = 0
        for row in pantries:
            PantryRecord(listFrame, row[0], row[1], row[2]).grid(column = 0, row = i)
            i+=1

        mydb.commit()

class PantryRecord(customtkinter.CTkFrame):

    def __init__(self, master, ID, name, address):

        customtkinter.CTkFrame.__init__(self, master, width = 775, height = 100, fg_color='white')

        self.placeDetails(ID, name, address)

    def placeDetails(self, ID, name, address):

        pantryID = customtkinter.CTkLabel(self, width = 154, height = 38, fg_color='white', text = ID, anchor='w')
        pantryID.place(x = 0, y = 13)

        pantryName = customtkinter.CTkLabel(self, width = 243, height = 38, fg_color='white', text = name, anchor='w')
        pantryName.place(x = 176, y = 13)

        pantryFirstAddress = customtkinter.CTkLabel(self, width = 300, height = 84, fg_color = 'white', text = address, anchor='nw', wraplength=250)
        pantryFirstAddress.place(x = 446, y = 23)
