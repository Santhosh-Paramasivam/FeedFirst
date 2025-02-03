import customtkinter
from PIL import Image
import constants.colour_constants as cc
from database.mysql_connection import mydb, mycursor
from utils.widgets import Error
from modules.pantry_details import PantryDetails
from modules.sign_up import SignUp

class LogIn(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)

        self.setBackground()
        self.placeWidgets()

    def placeWidgets(self):

        self.usernameField = customtkinter.CTkEntry(self, width=241, height=39, corner_radius=15, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.usernameField.place(x=406, y=384)

        self.passwordField = customtkinter.CTkEntry(self, width=241, height=39, corner_radius=15, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.passwordField.place(x=406, y=460)

        logInButton = customtkinter.CTkButton(self, fg_color=cc.darkPurple, text='Log In', width=120, height=42, command=self.logIn, text_color='white', corner_radius=20, bg_color='white', hover_color=cc.lightPurple)
        logInButton.place(x=213, y=544)

        pantryDetailsButton = customtkinter.CTkButton(self, fg_color=cc.darkPurple, text='Pantry Details',width=120, height=42, command=self.pantryDetails, text_color='white', corner_radius=20, bg_color='white', hover_color=cc.lightPurple)
        pantryDetailsButton.place(x=390, y=544)

        signupButton = customtkinter.CTkButton(self, fg_color=cc.darkPurple, text='Sign Up', width=120, height=42, command=self.signup, text_color='white', corner_radius=20, bg_color='white', hover_color=cc.lightPurple)
        signupButton.place(x=562, y=544)

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Recepient\LoginPage.png'),
                                                  dark_image=Image.open(r'images\Recepient\LoginPage.png'),
                                                  size=(900, 675))
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def signup(self):
        
        signup = SignUp(self)
        signup.place(x=0, y=0)

    def pantryDetails(self):

        pantryDetails = PantryDetails(self)
        pantryDetails.place(x = 0, y = 0)

    def logIn(self):

        global USERNAME
        global USER_RECEPIENT_ID

        username = self.usernameField.get()
        password = self.passwordField.get()

        mycursor.execute("""SELECT * 
                         FROM Recepients 
                         WHERE status = 'VALID' """)
        
        users = mycursor.fetchall()

        present = False
        for row in users:
            if(username == row[5] and password == row[6]): present = True

        errors = []

        if(present == False):
            errors.append("Username or Password Invalid")
            Error(self,errors)
            return
        else:
            USERNAME = username

            sql = "SELECT recepient_id FROM recepients WHERE username = %s"
        
            mycursor.execute(sql,(USERNAME,))
            value = mycursor.fetchall()
            USER_RECEPIENT_ID = value[0][0]

        mydb.commit()

        # foodVoucher = FoodVoucher(self)
        # foodVoucher.place(x = 0, y = 0)
