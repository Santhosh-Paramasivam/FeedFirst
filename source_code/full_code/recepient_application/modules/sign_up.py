import customtkinter
from PIL import Image
import constants.colour_constants as cc
from database.mysql_connection import mydb, mycursor
from utils.widgets import Error,FrameLeave
from utils.functions import is_integer

class SignUp(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)

        self.setBackground()
        self.placeWidgets()

    def placeWidgets(self):

        self.nameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12,fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.nameField.place(x=219, y=161)

        self.pnumberField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.pnumberField.place(x=219, y=220)

        self.addressField = customtkinter.CTkTextbox(self, width=171, height=106, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.addressField.place(x=219, y=290)

        self.houseSizeField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.houseSizeField.place(x=219, y=432)

        self.dietaryNeedsField = customtkinter.CTkTextbox(self, width=171, height=74, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.dietaryNeedsField.place(x=219, y=489)

        self.emailField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12,fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.emailField.place(x=219, y=588)

        self.houseRecepientsField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.houseRecepientsField.place(x=676, y=162)

        self.rationNumberField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.rationNumberField.place(x=676, y=258)

        self.usernameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.usernameField.place(x=676, y=316)

        self.passwordField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.passwordField.place(x=676, y=371)

        self.passRepeatField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.passRepeatField.place(x=676, y=426)

        self.pantryIDField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.pantryIDField.place(x=676, y=472)

        self.exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        self.exitButton.place(x = 530, y = 580)

        self.submitButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Submit', hover_color=cc.lightPurple, command = self.submit)
        self.submitButton.place(x = 702, y = 580)

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Recepient\SignUpPage.png'),
                                                  dark_image=Image.open(r'images\Recepient\SignUpPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def submit(self):

        errors = []

        name = self.nameField.get()
        pnumber = self.pnumberField.get()
        address = self.addressField.get(1.0, "end-1c")
        houseSize = self.houseSizeField.get()
        houseRecepients = self.houseRecepientsField.get()
        dietaryNeeds = self.dietaryNeedsField.get(1.0, "end-1c")
        email = self.emailField.get()
        rationNumber = self.rationNumberField.get()

        username = self.usernameField.get()
        password = self.passwordField.get()
        repeatPassword = self.passRepeatField.get()
        pantryID = self.pantryIDField.get()

        if(name == '' or
           pnumber == '' or
           address == '' or
           houseSize == '' or
           houseRecepients == '' or
           email == '' or
           rationNumber == '' or
           username == '' or
           password == '' or
           pantryID == ''): 
            errors.append("All fields other than dietary needs are mandatory")

        if(is_integer(pnumber) != True): errors.append("Phone number must be an integer")
        if(is_integer(rationNumber) != True): errors.append("Ration number must be an integer")

        if(len(pnumber) != 10): errors.append("Phone number must be 10 digits")
        if(len(rationNumber) != 10): errors.append("Ration number must be 10 digits")

        if(is_integer(houseSize) != True): errors.append("Household size must be an integer")

        if(password != repeatPassword): errors.append("Password and repeat password don't match")

        mycursor.execute("SELECT username from recepients")
        unavailableUsernames = mycursor.fetchall()

        for unavailableUsername in unavailableUsernames:
            if(unavailableUsername[0] == username):
                errors.append("Unavailable Username")

        mycursor.execute("SELECT * FROM Pantries")
        pantries = mycursor.fetchall()

        if(pantryID != ''):
            present = False
            for row in pantries:
                if(row[0] == int(pantryID)):
                    present = True
            
            if(present == False): errors.append("Invalid Pantry ID")

        if(len(errors) > 0):
            Error(self, errors)
            return

        sql = "INSERT INTO Recepients(phone_number,status,name,ration_card_number,username,password,household_member_names,email_ID,dietary_needs,household_size,pantry_ID,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (pnumber,"PENDING",name,rationNumber,username,password,houseRecepients,email,dietaryNeeds,houseSize,pantryID,address)

        mycursor.execute(sql, values)
        mydb.commit()

