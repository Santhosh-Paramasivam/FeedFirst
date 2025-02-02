import customtkinter
from PIL import Image

# COLOUR CONSTANTS ###############

darkPurple = '#0C1765'
lightPurple = '#505FC8'

# SPECIAL CLASSES ################

class TextFrame(customtkinter.CTkFrame):

    def __init__(self, master, width, height, text):

        customtkinter.CTkFrame.__init__(self, master,
                                        width = width,
                                        height= height,
                                        corner_radius=0,
                                        border_width=1,
                                        bg_color='white',
                                        border_color='gray'
                                        )
        
        text = customtkinter.CTkLabel(self, width, height, bg_color='white', fg_color='white', text_color='black', text = text)
        text.pack()

class DropOffRecord(customtkinter.CTkFrame):

    def __init__(self, master, ID, name, address1, address2, address3, address4):

        customtkinter.CTkFrame.__init__(self, master, width = 775, height = 142, fg_color='white')

        self.placeDetails(ID, name, address1, address2, address3, address4)

    def placeDetails(self, ID, name, address1, address2, address3, address4):

        dropOffID = customtkinter.CTkLabel(self, width = 154, height = 38, fg_color='white', text = ID, anchor='w')
        dropOffID.place(x = 0, y = 13)

        dropOffName = customtkinter.CTkLabel(self, width = 243, height = 38, fg_color='white', text = name, anchor='w')
        dropOffName.place(x = 176, y = 13)

        dropOffFirstAddress = customtkinter.CTkLabel(self, width = 300, height = 28, fg_color = 'white', text = address1, anchor='w')
        dropOffFirstAddress.place(x = 446, y = 13)

        dropOffSecondAddress = customtkinter.CTkLabel(self, width = 300, height = 28, fg_color = 'white', text = address2, anchor='w')
        dropOffSecondAddress.place(x = 446, y = 41)

        dropOffThirdAddress = customtkinter.CTkLabel(self, width = 300, height = 28, fg_color = 'white', text = address3, anchor='w')
        dropOffThirdAddress.place(x = 446, y = 69)

        dropOffFourthAddress = customtkinter.CTkLabel(self, width = 300, height = 28, fg_color = 'white', text = address4, anchor='w')
        dropOffFourthAddress.place(x = 446, y = 97)

class ItemRecord(customtkinter.CTkFrame):

    def __init__(self, master, item, need, units):

        customtkinter.CTkFrame.__init__(self, master, width = 775, height = 50, fg_color='white')

        self.placeDetails(item, need, units)

    def placeDetails(self, item, need, units):

        itemLabel = customtkinter.CTkLabel(self, width = 210, height = 38, fg_color='white', text = item, anchor='center')
        itemLabel.place(x = 0, y = 7)  

        needLabel = customtkinter.CTkLabel(self, width = 210, height = 38, fg_color='white', text = need, anchor='center')
        needLabel.place(x = 252, y = 7)

        unitsLabel = customtkinter.CTkLabel(self, width = 210, height = 38, fg_color='white', text = units, anchor='center')
        unitsLabel.place(x = 525, y = 7)          

        

class DonationRecord(customtkinter.CTkFrame):

    def __init__(self, master, ID, date, location, items, description, status):

        customtkinter.CTkFrame.__init__(self, master, width = 775, height = 268, fg_color='white')

        self.placeDetails(ID, date, location, items, description, status)

    def placeDetails(self, ID, date, location, items, description, status):

        donationID = TextFrame(self, width = 161, height = 30, text = ID)
        donationID.grid(row = 0, column = 0)

        donationDate = TextFrame(self, width = 161, height = 30, text = 'On ' + date)
        donationDate.grid(row = 1, column = 0)

        donationLocation = TextFrame(self, width = 161, height = 30, text = 'At ' + location)
        donationLocation.grid(row = 2, column = 0)

        for i in range(0, len(items),1):
            donationItem = TextFrame(self, width = 257, height = 30, text = str(items[i][0]) + " - " + str(items[i][1]))
            donationItem.grid(row = i, column = 1)

        #donationDescription = TextFrame(self, width = 165, height = 150, text = description)
        #donationDescription.grid(row = 0, column = 2, rowspan = 5)

        donationDescription = customtkinter.CTkLabel(self, width = 210, height = 150, text = description, wraplength=208, anchor='center', font=('Calibri',15))
        donationDescription.grid(row = 0, column = 2, rowspan = 5)

        donationStatus = TextFrame(self, width = 161, height = 30, text = status)
        donationStatus.grid(row = 0, column = 3)

    


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

# MAIN CLASS #####################

class FeedFirstDonor(customtkinter.CTk):

    def __init__(self):

        customtkinter.CTk.__init__(self)
        self.geometry('900x675')
        self.title('FeedFirstDonor')

        Login(self).place(x = 0, y = 0)

# PAGE CLASSES ###################

class Login(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width = 900, height = 675)
        
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Recepient\LoginPage.png'),
                                                  dark_image=Image.open(r'images\Recepient\LoginPage.png'),
                                                  size=(900, 675))
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        usernameField = customtkinter.CTkEntry(self, width=241, height=39, corner_radius=15, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        usernameField.place(x=406, y=384)

        passwordField = customtkinter.CTkEntry(self, width=241, height=39, corner_radius=15, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        passwordField.place(x=406, y=460)

        logInButton = customtkinter.CTkButton(self, fg_color=darkPurple, text='Log In', width=120, height=42, text_color='white', corner_radius=20, bg_color='white', hover_color=lightPurple, command = self.login)
        logInButton.place(x=95, y=543)

        dropLocationButton = customtkinter.CTkButton(self, fg_color=darkPurple, text='Drop Off Locations',width=164, height=44, text_color='white', corner_radius=20, bg_color='white', hover_color=lightPurple, command = self.dropOffDetails)
        dropLocationButton.place(x=245, y=542)

        individualSUButton = customtkinter.CTkButton(self, fg_color=darkPurple, text='Individual Sign Up',width=164, height=44, text_color='white', corner_radius=20, bg_color='white', hover_color=lightPurple, command = self.signUpIndividual)
        individualSUButton.place(x=442, y=542)

        organizationSUButton = customtkinter.CTkButton(self, fg_color=darkPurple, text='Organization Sign Up',width=164, height=44, text_color='white', corner_radius=20, bg_color='white', hover_color=lightPurple, command = self.signUpOrganization)
        organizationSUButton.place(x=639, y=542)

    def signUpIndividual(self):

        signUpIndividual = SignUpIndividual(self)
        signUpIndividual.place(x = 0, y = 0)

    def signUpOrganization(self):

        signUpOrganization = SignUpOrganization(self)
        signUpOrganization.place(x = 0, y = 0)

    def dropOffDetails(self):

        dropOffDetails = DropOffDetails(self)
        dropOffDetails.place(x = 0, y = 0)

    def login(self):

        donationList = DonationList(self)
        donationList.place(x = 0, y = 0)


class SignUpIndividual(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width = 900, height = 675, corner_radius = 0)
        
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Donor\SignUpPerson.png'),
                                                  dark_image=Image.open(r'images\Donor\SignUpPerson.png'),
                                                  size=(900, 675))
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        nameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        nameField.place(x=219, y=161)

        phoneNumberField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        phoneNumberField.place(x=219, y=222)

        emailIDField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        emailIDField.place(x=219, y=286)

        addressField = customtkinter.CTkTextbox(self, width=171, height=110, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        addressField.place(x=219, y=356)

        rationNumberField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        rationNumberField.place(x=219, y=507)

        usernameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        usernameField.place(x=669, y=158)

        passwordField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        passwordField.place(x=669, y=213)

        repeatPasswordField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        repeatPasswordField.place(x=669, y=268)

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Exit', hover_color=lightPurple)
        exitButton.place(x = 530, y = 400)

        signUpButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Sign Up', hover_color=lightPurple)
        signUpButton.place(x = 702, y = 400)

class SignUpOrganization(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width = 900, height = 675, corner_radius = 0)
        
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Donor\SignUpOrganization.png'),
                                                  dark_image=Image.open(r'images\Donor\SignUpOrganization.png'),
                                                  size=(900, 675))
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        institutionTypes = ['Supermarkets','Restaurants','Farms']

        institutionNameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        institutionNameField.place(x=224, y=177)

        institutionTypeField = customtkinter.CTkComboBox(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white', values = institutionTypes, dropdown_fg_color='white', dropdown_hover_color='gray')
        institutionTypeField.place(x=224, y=235)

        contactNameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        contactNameField.place(x=224, y=300)

        contactPositionField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        contactPositionField.place(x=224, y=369)

        contactEmailField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        contactEmailField.place(x=224, y=448)

        contactPNumberField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        contactPNumberField.place(x=224, y=528)

        institutionAddressField = customtkinter.CTkTextbox(self, width=171, height=98, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        institutionAddressField.place(x=670, y=156)

        businessPanField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        businessPanField.place(x=670, y=284)

        usernameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        usernameField.place(x=670, y=346)

        passwordField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        passwordField.place(x=670, y=401)

        repeatPasswordField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        repeatPasswordField.place(x=670, y=456)

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Exit', hover_color=lightPurple)
        exitButton.place(x = 530, y = 580)

        signUpButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Sign Up', hover_color=lightPurple)
        signUpButton.place(x = 702, y = 580)

class DonationList(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width = 900, height = 675, corner_radius = 0)

        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Donor\DonationListPage.png'),
                                                  dark_image=Image.open(r'images\Donor\DonationListPage.png'),
                                                  size=(900, 675))
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Exit', hover_color=lightPurple)
        exitButton.place(x = 487, y = 587)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 775, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 57, y = 180)

        items = [['Canned Beans',1],['Canned Beans',1],['Canned Beans',1],['Canned Beans',1],['Canned Beans',1],['Canned Beans',1],['Canned Beans',1],['Canned Beans',1],['Canned Beans',1]]

        donateButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Donate', hover_color=lightPurple, command = self.donate)
        donateButton.place(x = 261, y = 588)

        d1 = DonationRecord(listFrame, "DON001", "12/07/2024","LOC001", items, "This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill,This is not a drill", "Pending")
        d1.grid(row = 0, column = 0)

    def donate(self):

        donate = Donate(self)
        donate.place(x = 0, y = 0)

class Donate(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width = 900, height = 675, corner_radius = 0)

        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Donor\DonationPage.png'),
                                                  dark_image=Image.open(r'images\Donor\DonationPage.png'),
                                                  size=(900, 675))
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack() 

    def placeWidgets(self):

        items = ['','Applesauce',
                 'Peanut butter',
                 'Canned beans',
                 'Canned chicken',
                 'Canned fish',
                 'Canned meat',
                 'Canned vegetables',
                 'Cooking oil',
                 'Crackers',
                 'Dried herbs and spices',
                 'Canned fruits',
                 'Granola bars',
                 'Nuts',
                 'Pasta',
                 'Rice',
                 'Powdered milk'
        ]     

        itemVars = []   
        quantityEntries = []
        expiryEntries = []

        height = 35
        for i in range(0, 9, 1):
            itemVar = customtkinter.StringVar()
            customtkinter.CTkComboBox(self, width = 233, height = 35, corner_radius = 10, border_width=1, bg_color='white', fg_color='white', border_color='gray', values=items, variable=itemVar, dropdown_fg_color='white').place(x = 81, y = 192 + (height * i))
            itemVars.append(itemVar)
            quantityEntry = customtkinter.CTkEntry(self, width = 112, height = 35, corner_radius = 10, border_width=1, bg_color='white',fg_color='white', border_color='gray').place(x = 315, y = 192 + (height * i))
            quantityEntries.append(quantityEntry)
            expiryEntry = customtkinter.CTkEntry(self, width = 140, height = 35, corner_radius = 10, border_width=1, bg_color='white',fg_color='white', border_color='gray').place(x = 676, y = 192 + (height * i))
            expiryEntries.append(expiryEntry)

        descriptionField = customtkinter.CTkTextbox(self, width=232, height=180, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        descriptionField.place(x=435, y=192)  

        amountsAndUnitsButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Need and Units', hover_color=lightPurple, command = self.amountsAndUnits)
        amountsAndUnitsButton.place(x = 201, y = 586)  

        donateButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Donate', hover_color=lightPurple)
        donateButton.place(x = 387, y = 586)      

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Exit', hover_color=lightPurple)
        exitButton.place(x = 563, y = 587)   

    def amountsAndUnits(self):

        amountsAndUnits = ItemDetails(self)
        amountsAndUnits.place(x = 0, y = 0)

class DropOffDetails(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)
        
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Donor\DropOffPage.png'),
                                                  dark_image=Image.open(r'images\Donor\DropOffPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Exit', hover_color=lightPurple)
        exitButton.place(x = 385, y = 587)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 775, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 57, y = 180)

        dropOff1 = DropOffRecord(listFrame, 'PAN01', 'Vinay Pantry', '20, T.S.N Avenue,','K.K.Nagar,','Tiruchirapalli','Tamil Nadu - 620007')
        dropOff1.grid(column = 0, row = 0)

        dropOff2 = DropOffRecord(listFrame, 'PAN02', 'Senabadhy Pantry', 'SRM Nagar,','Irungulur, Chennai Highway','Tiruchirapalli','Tamil Nadu - 621105')
        dropOff2.grid(column = 0, row = 1)

        dropOff3 = DropOffRecord(listFrame, 'PAN03', 'Riddhisha Pantry', 'BHEL Apartments','Williams Road, Near Central Bus Stand','Tiruchirapalli','Tamil Nadu - 621105')
        dropOff3.grid(column = 0, row = 2)

class ItemDetails(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)
        
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Donor\Units.png'),
                                                  dark_image=Image.open(r'images\Donor\Units.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=darkPurple,text_color='white', text='Exit', hover_color=lightPurple)
        exitButton.place(x = 385, y = 587)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 775, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 57, y = 180)

        dropOff1 = ItemRecord(listFrame, 'Nutella', 'Very High', 'jars')
        dropOff1.grid(column = 0, row = 0)

        dropOff2 = ItemRecord(listFrame, 'Cooking Oil', 'Low', 'litres / l')
        dropOff2.grid(column = 0, row = 1)

        dropOff3 = ItemRecord(listFrame, 'Rice', 'High', 'kilograms / kg')
        dropOff3.grid(column = 0, row = 2)


# MAIN FUNCTION #####################

def main():

    FF = FeedFirstDonor()
    FF.mainloop()

if __name__ == '__main__':
    main()