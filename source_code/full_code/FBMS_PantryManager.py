import customtkinter
from PIL import Image
from datetime import date,datetime

from utils.widgets import FrameLeave, Error
from utils.functions import is_integer

import mysql.connector

import os
from dotenv import load_dotenv

import constants.colour_constants as cc

# LOADING ENVIRONMENT VARIABLES

load_dotenv()

# MYSQL CONNECTION  ##############

mydb = mysql.connector.connect(
  host="localhost",
  user=os.getenv("USERNAME"),
  password=os.getenv("PASSWORD"),
  database="FeedFirst"
)

mycursor = mydb.cursor()

# GLOBAL VARIABLES ###############

global USERNAME
global PANTRY_ID

# SPECIAL CLASSES  ###############

class VoucherRecord(customtkinter.CTkFrame):

    def __init__(self, frameMaster, frame, master, ID, recepientName, status, priority):

        customtkinter.CTkFrame.__init__(self, master, width = 775, height = 55, fg_color='white')

        self.frameMaster = frameMaster
        self.frame = frame
        self.voucherID = ID

        self.placeDetails(ID, recepientName, status, priority)

    def placeDetails(self, ID, recepientName, status, priority):

        IDLabel = customtkinter.CTkLabel(self, width = 100, height = 38, fg_color='white', text = ID, anchor='w')
        IDLabel.place(x = 0, y = 4)  

        recepientNameLabel = customtkinter.CTkLabel(self, width = 176, height = 38, fg_color='white', text = recepientName, anchor='w')
        recepientNameLabel.place(x = 127, y = 4)

        statusLabel = customtkinter.CTkLabel(self, width = 125, height = 38, fg_color='white', text = status, anchor='w')
        statusLabel.place(x = 330, y = 4)  

        priorityLabel = customtkinter.CTkLabel(self, width = 146, height = 38, fg_color='white', text = priority, anchor='w')
        priorityLabel.place(x = 472, y = 4)  

        viewButton = customtkinter.CTkButton(self, width = 125, height = 38, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='View', hover_color=cc.lightPurple, command = self.view)
        viewButton.place(x = 641, y = 4)

    def view(self):

        ValidateVoucher(self.frameMaster,self.frame, self.voucherID).place(x = 0, y = 0)

class ItemAndUnitsRecord(customtkinter.CTkFrame):

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


# PAGE CLASSES ###################

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

        logInButton = customtkinter.CTkButton(self, fg_color=cc.darkPurple, text='Log In', width=120, height=42, text_color='white', corner_radius=20, bg_color='white', hover_color=cc.lightPurple, command = self.pantryInventory)
        logInButton.place(x=388, y=544)

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Pantry\LoginPage.png'),
                                                  dark_image=Image.open(r'images\Pantry\LoginPage.png'),
                                                  size=(900, 675))
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def pantryInventory(self):

        global USERNAME

        username = self.usernameField.get()
        password = self.passwordField.get()

        mycursor.execute("SELECT * FROM pantrymanager")
        
        users = mycursor.fetchall()

        present = False
        for row in users:
            if(username == row[0] and password == row[1]): present = True

        errors = []

        if(present == False):
            errors.append("Username or Password Invalid")
            Error(self,errors)
            return
        else:
            USERNAME = username


        PantryInventory(self).place(x = 0, y = 0)

class PantryInventory(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675, bg_color='white')

        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Pantry\PantryPage.png'),
                                                  dark_image=Image.open(r'images\Pantry\PantryPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        global USERNAME
        global PANTRY_ID

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 695, y = 588)

        verifyRecepientsButton = customtkinter.CTkButton(self, width = 138, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Verify Users', hover_color=cc.lightPurple, command = self.validateRecepient)
        verifyRecepientsButton.place(x = 362, y = 588)

        addPantryManagersButton = customtkinter.CTkButton(self, width = 138, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Add Employees', hover_color=cc.lightPurple, command = self.employeeEntry)
        addPantryManagersButton.place(x = 525, y = 588)

        itemsAndUnitsButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Items and Units', hover_color=cc.lightPurple, command = self.itemsAndUnits)
        itemsAndUnitsButton.place(x = 68, y = 588)

        deliverFoodButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Deliver Food', hover_color=cc.lightPurple, command = self.validateVouchers)
        deliverFoodButton.place(x = 219, y = 588)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 800, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 30, y = 180)

        mycursor.execute('SELECT pantry_ID FROM pantrymanager WHERE username = %s',(USERNAME,))
        data = mycursor.fetchall()
        PANTRY_ID = data[0][0]

        mycursor.execute("SELECT * FROM item WHERE pantry_ID = %s", (PANTRY_ID,))
        items = mycursor.fetchall()

        i = 0
        for item in items:
            ItemRecord(listFrame, item[0], item[4]).grid(column = 0, row = i)
            print(item[0],item[4])
            i+=1


    def validateRecepient(self):
        
        mycursor.execute("SELECT name,phone_number,address,household_size, ration_card_number FROM recepients WHERE status = 'PENDING'")
        self.recepients = mycursor.fetchall()
        print(self.recepients)

        self.recepientsIndex = len(self.recepients) - 1
        self.recepientNumber = len(self.recepients)

        if(self.recepientsIndex < 0):
            Error(self, ['No pending user requests at the moment!'])
            return
        
        ValidateRecepient(self).place(x = 0, y = 0)

    def validateVouchers(self):

        VoucherList(self).place(x = 0, y = 0)

    def itemsAndUnits(self):

        ItemDetails(self).place(x = 0, y = 0)

    def employeeEntry(self):

        EmployeeEntry(self).place(x = 0, y = 0)


class ItemRecord(customtkinter.CTkFrame):

    def __init__(self, master, itemID, itemName):

        global PANTRY_ID

        customtkinter.CTkFrame.__init__(self, master, width = 782, height = 267, fg_color='white', border_width=1, corner_radius=0)

        mycursor.execute("SELECT * FROM pantryitembatches WHERE pantry_ID = %s AND item_ID = %s", (PANTRY_ID,itemID))
        itemBatches = mycursor.fetchall()

        self.placeDetails(itemID, itemName, itemBatches)

    def placeDetails(self, itemID, itemName, itemBatches):

        itemID = customtkinter.CTkLabel(self, width = 215, height = 30, fg_color='white', text = itemID, anchor='w')
        itemID.place(x = 26, y = 8)

        itemName = customtkinter.CTkLabel(self, width = 215, height = 30, fg_color='white', text = itemName, anchor='w')
        itemName.place(x = 26, y = 38)

        yi = 30
        y = 10
        for i in range(0, len(itemBatches), 1):
            customtkinter.CTkLabel(self, width = 152, height = 30, fg_color='white', text = "Batch - " + str(itemBatches[i][2]), anchor='w').place(x = 238, y = y)
            y+=yi

        y = 10
        for i in range(0, len(itemBatches), 1):
            customtkinter.CTkLabel(self, width = 138, height = 30, fg_color='white', text = str(itemBatches[i][4]), anchor='w').place(x = 391, y = y)
            y+=yi

        y = 10
        for i in range(0, len(itemBatches), 1):
            customtkinter.CTkLabel(self, width = 140, height = 30, fg_color='white', text = itemBatches[i][3], anchor='w').place(x = 529, y = y)
            y+=yi
            
       

class ValidateRecepient(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)

        self.setBackground()
        self.placeWidgets()

    def placeWidgets(self):

        mycursor.execute("SELECT name,phone_number,address,household_size, ration_card_number, username FROM recepients WHERE status = 'PENDING'")
        self.recepients = mycursor.fetchall()
        
        self.recepientsIndex = len(self.recepients) - 1
        self.recepientNumber = len(self.recepients)

        priorities = ['Low','Medium','High']
        priorityVar = customtkinter.StringVar()

        self.nameLabel = customtkinter.CTkLabel(self, width = 300, height = 38, fg_color='white', text = 'Santhosh', anchor='w', font=('Default',15), bg_color='white')
        self.nameLabel.place(x = 453, y = 160)

        self.pnumberLabel = customtkinter.CTkLabel(self, width = 154, height = 38, fg_color='white', text = '9942927419', anchor='w', font=('Default',15), bg_color='white')
        self.pnumberLabel.place(x = 453, y = 208)

        self.addressLabel = customtkinter.CTkLabel(self, width = 200, height = 106, fg_color='white', text = 'BHEL Apartments, Williams Road, Near Central Bus Stand, Tiruchirapalli, Tamil Nadu - 621105', anchor= 'nw', font=('Default',13), wraplength=200, bg_color='white')
        self.addressLabel.place(x = 453, y = 278)

        self.householdSizeLabel = customtkinter.CTkLabel(self, width = 154, height = 38, fg_color='white', text = 'household size', anchor='w', font=('Default',15), bg_color='white')
        self.householdSizeLabel.place(x = 453, y = 402)

        self.unvalidatedRecepientsNumLabel = customtkinter.CTkLabel(self, width = 70, height = 30, fg_color='white', text = 'household size', anchor='w', font=('Default',15), bg_color='white')
        self.unvalidatedRecepientsNumLabel.place(x = 135, y = 185)

        self.rationCardLabel = customtkinter.CTkLabel(self, width = 154, height = 38, fg_color='white', text = 'ration card number', anchor='w', font=('Default',15), bg_color='white')
        self.rationCardLabel.place(x = 453, y = 462)

        self.priorityField = customtkinter.CTkComboBox(self, width=171, height=28, corner_radius=12,fg_color='white', border_width=1, border_color='gray', bg_color='white', values=priorities, variable=priorityVar)
        self.priorityField.place(x=452, y=520)        

        approveButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Approve', hover_color=cc.lightPurple, command = lambda : self.approve(priorityVar.get().upper()))
        approveButton.place(x = 306, y = 575)

        rejectButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Reject', hover_color=cc.lightPurple, command = self.reject)
        rejectButton.place(x = 476, y = 575)

        self.iterateRecepients()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Pantry\RecepientValidationPage.png'),
                                                  dark_image=Image.open(r'images\Pantry\RecepientValidationPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def approve(self, priority):

        if(priority == ''):
            Error(self, ['Enter a priority level!'])
            return
        
        sql = "UPDATE recepients SET status = 'VALID' WHERE username = %s"
        mycursor.execute(sql, (self.recepients[self.recepientsIndex][5],))

        print(priority)
        sql = "UPDATE recepients SET priority = %s WHERE username = %s"
        mycursor.execute(sql, (priority, self.recepients[self.recepientsIndex][5]))

        mydb.commit()
        self.iterateRecepients()

        if(self.recepientsIndex < -1):
            self.destroy()

    def reject(self):
           
        sql = "DELETE FROM recepients WHERE username = %s"
        mycursor.execute(sql, (self.recepients[self.recepientsIndex][5],))

        mydb.commit()
        self.iterateRecepients()

        if(self.recepientsIndex < -1):
            self.destroy()

    def iterateRecepients(self):

        recepient = self.recepients[self.recepientsIndex]

        self.nameLabel.configure(text = recepient[0])
        self.pnumberLabel.configure(text = recepient[1])
        self.addressLabel.configure(text = recepient[2])
        self.householdSizeLabel.configure(text = recepient[3])
        self.unvalidatedRecepientsNumLabel.configure(text = self.recepientNumber)
        self.rationCardLabel.configure(text = recepient[4])
    
        self.recepientsIndex-=1
        self.recepientNumber-=1

class VoucherList(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)

        self.master = master

        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Pantry\VoucherListPage.png'),
                                                  dark_image=Image.open(r'images\Pantry\VoucherListPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        global PANTRY_ID

        # STATUSES : PENDING, APPROVED, PROVIDED, REJECTED

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 385, y = 587)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 781, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 50, y = 180)

        mycursor.execute("SELECT * FROM foodvouchers WHERE pantry_ID = %s", (PANTRY_ID,))
        vouchers = mycursor.fetchall()
        
        i = 0
        for voucher in vouchers:
            voucherID = voucher[1]
            voucherStatus = voucher[2]
            recepientID = voucher[0]
            
            sql = "SELECT name,priority FROM recepients WHERE recepient_id = %s"
            mycursor.execute(sql, (recepientID,))
            data = mycursor.fetchall()
            recepientName = data[0][0]
            recepientPriority = data[0][1]
            VoucherRecord(self.master, self, listFrame, voucherID, recepientName, voucherStatus, recepientPriority).grid(column = 0, row = i)
            i+=1

class ValidateVoucher(customtkinter.CTkFrame):

    # VOUCHERS : PENDING, APPROVED, REJECTED, PROVIDED

    def __init__(self, frameMaster, master, voucherID):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)

        self.voucherID = voucherID
        self.frameMaster = frameMaster
        self.stop = False

        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Pantry\VoucherValidationPage.png'),
                                                  dark_image=Image.open(r'images\Pantry\VoucherValidationPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        self.itemNames = []
        self.itemIDs = []

        mycursor.execute('SELECT pantry_ID FROM pantrymanager WHERE username = %s',(USERNAME,))
        data = mycursor.fetchall()
        pantry_ID = data[0][0]

        mycursor.execute("SELECT * FROM item WHERE pantry_ID = %s", (pantry_ID,))

        items = mycursor.fetchall()
        for item in items:
            self.itemNames.append(item[4])
            self.itemIDs.append(item[0])

        sql = "SELECT recepient_ID,status FROM foodvouchers WHERE voucher_id = %s"
        mycursor.execute(sql, (self.voucherID,))
        data = mycursor.fetchall()

        recepientID = data[0][0]
        voucherStatus = data[0][1]
    
        sql = "SELECT name, household_size, priority, dietary_needs FROM recepients WHERE recepient_ID = %s"
        mycursor.execute(sql, (recepientID,))
        data = mycursor.fetchall()

        name = data[0][0]
        householdSize = data[0][1]
        priority = data[0][2]
        dietaryNeeds = data[0][3]

        nameLabel = customtkinter.CTkLabel(self, width = 200, height = 28, fg_color='white', text = name, anchor='w', font=('Default',15), bg_color='white')
        nameLabel.place(x = 219, y = 175)   

        householdSizeLabel = customtkinter.CTkLabel(self, width = 200, height = 28, fg_color='white', text = householdSize, anchor='w', font=('Default',15), bg_color='white')
        householdSizeLabel.place(x = 219, y = 232)   

        priorityLabel = customtkinter.CTkLabel(self, width = 200, height = 28, fg_color='white', text = priority, anchor='w', font=('Default',15), bg_color='white')
        priorityLabel.place(x = 219, y = 286)   
        
        dietaryNeedsLabel = customtkinter.CTkLabel(self, width = 200, height = 106, fg_color='white', text = dietaryNeeds, anchor= 'nw', font=('Default',13), wraplength=200, bg_color='white')
        dietaryNeedsLabel.place(x = 219, y = 346) 

        sql = "SELECT * FROM requesteditem WHERE voucher_id = %s"
        mycursor.execute(sql, (self.voucherID,))
        items = mycursor.fetchall()
        self.itemNamesDisplay = [] 
        self.requestedQuantities = []
        self.itemVoucherIDs = []
        providedQuantities = []

        for item in items:
            self.itemNamesDisplay.append(self.itemNames[self.itemIDs.index(item[0])])
            self.requestedQuantities.append(item[2])
            providedQuantities.append(item[3])
            self.itemVoucherIDs.append(item[4])

        itemAndQuantityFrame = customtkinter.CTkScrollableFrame(self, width = 344, height = 412, fg_color='white', bg_color='white')
        itemAndQuantityFrame.place(x = 503, y = 141)

        self.item1 = customtkinter.StringVar()
        self.item2 = customtkinter.StringVar()
        self.item3 = customtkinter.StringVar()
        self.item4 = customtkinter.StringVar()
        self.item5 = customtkinter.StringVar()
        self.item6 = customtkinter.StringVar()
        self.item7 = customtkinter.StringVar()
        self.item8 = customtkinter.StringVar()

        self.quantity1 = customtkinter.StringVar()
        self.quantity2 = customtkinter.StringVar()
        self.quantity3 = customtkinter.StringVar()
        self.quantity4 = customtkinter.StringVar()
        self.quantity5 = customtkinter.StringVar()
        self.quantity6 = customtkinter.StringVar()
        self.quantity7 = customtkinter.StringVar()
        self.quantity8 = customtkinter.StringVar()

        self.itemVars = [self.item1, self.item2,self.item3, self.item4,self.item5, self.item6,self.item7, self.item8]
        self.quantityVars = [self.quantity1, self.quantity2,self.quantity3, self.quantity4,self.quantity5, self.quantity6,self.quantity7, self.quantity8]

        j = 0
        k = 0
        l = 0
        for i in range(0,16,1):
            if(i%2==0):
                customtkinter.CTkLabel(itemAndQuantityFrame, width = 140, height = 38, anchor = 'e', text = 'Item ' + str(j+1) + ':         ').grid(row = i, column = 0)
                customtkinter.CTkEntry(itemAndQuantityFrame, width = 180, height = 30, textvariable = self.itemVars[j], state = customtkinter.DISABLED).grid(row = i, column = 1)
                j+=1
            else:
                customtkinter.CTkLabel(itemAndQuantityFrame, width = 140, height = 38, anchor = 'e', text = 'Quantity ' + str(j) + ' :         ').grid(row = i, column = 0)
                customtkinter.CTkEntry(itemAndQuantityFrame, width = 180, height = 30, textvariable = self.quantityVars[k]).grid(row = i, column = 1)
                k+=1

        i = 0
        for itemName in self.itemNamesDisplay:
            self.itemVars[i].set(itemName)
            i+=1

        if(voucherStatus == 'PENDING' or voucherStatus == 'REJECTED'):
            i = 0
            for requestedQuantity in self.requestedQuantities:
                self.quantityVars[i].set(requestedQuantity)
                i+=1
        
        elif(voucherStatus == 'APPROVED' or voucherStatus == 'PROVIDED'):
            i = 0
            for providedQuantity in providedQuantities:
                self.quantityVars[i].set(providedQuantity)
                i+=1

        if(voucherStatus == 'PENDING'):
            rejectButton = customtkinter.CTkButton(self, width = 141, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Reject Voucher', hover_color=cc.lightPurple, command = lambda voucherID = self.voucherID : self.changeVoucherStatus(voucherID,'REJECTED'))
            rejectButton.place(x = 514, y = 582)

            approveButton = customtkinter.CTkButton(self, width = 141, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Approve Voucher', hover_color=cc.lightPurple, command = self.approve)
            approveButton.place(x = 694, y = 582)

        elif(voucherStatus == 'PROVIDED' or voucherStatus == 'REJECTED'):
            pass

        elif(voucherStatus == 'APPROVED'):
            provideButton = customtkinter.CTkButton(self, width = 141, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Provide Food', hover_color=cc.lightPurple, command = lambda voucherID = self.voucherID : self.changeVoucherStatus(voucherID,'PROVIDED'))
            provideButton.place(x = 694, y = 582)

        exitButton = FrameLeave(self, width = 141, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 154, y = 572)

    def approve(self):

        errors = []
        itemBatchQuantities = []
        itemBatchIDs = []

        self.stop = False
        for i in range(0,len(self.itemNamesDisplay),1):
            itemName = self.itemNamesDisplay[i]
            print(itemName)
            mycursor.execute("SELECT item_ID FROM item WHERE item_name = %s", (itemName,))
            itemID = mycursor.fetchall()[0][0]
            print(itemID)
            mycursor.execute("SELECT * FROM pantryitembatches WHERE pantry_ID = %s AND item_ID = %s", (PANTRY_ID,itemID))
            itemBatches = mycursor.fetchall()
            for itemBatch in itemBatches:
                itemBatchQuantity = itemBatch[4]
                itemBatchID = itemBatch[1]
                itemBatchQuantities.append(itemBatchQuantity)
                itemBatchIDs.append(itemBatchID)

            itemBatchQuantities = self.removeStock(itemBatchQuantities, int(self.quantityVars[i].get()))

            if(self.stop == True):
                errors.append("Insufficient Stock")
                Error(self, errors)
                return
            
        for i in range(0,len(self.itemNamesDisplay),1):
            itemBatchIDs = []
            itemBatchQuantities = []
            itemName = self.itemNamesDisplay[i]
            print(itemName)
            mycursor.execute("SELECT item_ID FROM item WHERE item_name = %s", (itemName,))
            itemID = mycursor.fetchall()[0][0]
            print(itemID)
            mycursor.execute("SELECT * FROM pantryitembatches WHERE pantry_ID = %s AND item_ID = %s", (PANTRY_ID,itemID))
            itemBatches = mycursor.fetchall()
            print("-", itemBatches)
            for itemBatch in itemBatches:
                itemBatchQuantity = itemBatch[4]
                itemBatchID = itemBatch[1]
                itemBatchQuantities.append(itemBatchQuantity)
                itemBatchIDs.append(itemBatchID)

            itemBatchQuantities = self.removeStock(itemBatchQuantities, int(self.quantityVars[i].get()))

            for i in range(0, len(itemBatchIDs),1):
                if(itemBatchQuantities[i] == 0):
                    mycursor.execute("delete from pantryitembatches where batch_id = %s", (itemBatchIDs[i],))
                else:
                    mycursor.execute("update pantryitembatches set quantity = %s where batch_id = %s", (itemBatchQuantities[i],itemBatchIDs[i]))
                mydb.commit()
        
        itemBatches = mycursor.fetchall()

        i = 0
        for itemName in self.itemNamesDisplay:
            providedQuantity = self.quantityVars[i].get()
            itemVoucherID = self.itemVoucherIDs[i]

            sql = "UPDATE requesteditem SET provided_quantity = %s WHERE voucher_item_ID = %s"
            mycursor.execute(sql, (providedQuantity, itemVoucherID))
            mydb.commit()
            i+=1
        
        x = lambda voucherID = self.voucherID : self.changeVoucherStatus(voucherID,'APPROVED')
        x()
        pass

    def changeVoucherStatus(self, voucherID, status):

        sql = "UPDATE foodvouchers SET status = %s WHERE voucher_id = %s"
        mycursor.execute(sql, (status, voucherID))

        mydb.commit()

        VoucherList(master = self.frameMaster).place(x = 0, y = 0)
        self.master.destroy()
        
    def removeStock(self, stockQuantities, removalQuantity):

        for i in range(0, len(stockQuantities),1):
            print('q',removalQuantity,'\t','s',stockQuantities)
            if(removalQuantity == 0):
                break
            elif(stockQuantities[i] > removalQuantity):
                stockQuantities[i] -= removalQuantity
                removalQuantity = 0
            elif(stockQuantities[i] == removalQuantity):
                stockQuantities[i] = 0
                removalQuantity = 0
            elif(stockQuantities[i] < removalQuantity):
                removalQuantity -= stockQuantities[i]
                stockQuantities[i] = 0

        if(removalQuantity != 0):
            self.stop = True
        else:
            return stockQuantities

            
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

        global PANTRY_ID

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 385, y = 587)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 775, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 57, y = 180)

        addItems = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Add Items', hover_color=cc.lightPurple, command = self.addItems)
        addItems.place(x = 250, y = 587)

        addBatches = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Add Item Batches', hover_color=cc.lightPurple, command = self.addItemBatches)
        addBatches.place(x = 510, y = 587)

        mycursor.execute("SELECT * FROM item WHERE pantry_ID = %s", (PANTRY_ID,))
        items = mycursor.fetchall()

        i = 0
        for item in items:
            ItemAndUnitsRecord(listFrame, item[4], item[3], item[1]).grid(column = 0, row = i)
            i+=1

    def addItems(self):

        AddItem(self).place(x = 0, y = 0)

    def addItemBatches(self):

        AddItemBatches(self).place(x = 0, y = 0)

class AddItem(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)

        self.master = master
        
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Pantry\AddItems.png'),
                                                  dark_image=Image.open(r'images\Pantry\AddItems.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        stockLevels = ['Low','Medium','High']
        self.stockLevelVar = customtkinter.StringVar()

        itemUnits = ['g / grams', 'kg / kilograms']
        self.itemUnitsVar = customtkinter.StringVar()

        mycursor.execute("select item_name from item")
        items = mycursor.fetchall()

        itemNames = []
        for item in items:
            itemNames.append(item[0])

        self.itemNameVar = customtkinter.StringVar()

        self.itemName = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.itemName.place(x=218, y=148)

        self.itemUnits = customtkinter.CTkComboBox(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white', values = itemUnits, variable = self.itemUnitsVar)
        self.itemUnits.place(x=632, y=148)

        self.itemName1 = customtkinter.CTkComboBox(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white', values = itemNames, variable = self.itemNameVar)
        self.itemName1.place(x=218, y=345)

        self.stockLevel = customtkinter.CTkComboBox(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white', values = stockLevels, variable = self.stockLevelVar)
        self.stockLevel.place(x=632, y=345)

        self.exitButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple, command = self.exit)
        self.exitButton.place(x = 385, y = 587)

        self.changeStockButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Change Stock', hover_color=cc.lightPurple, command = self.changeItemStock)
        self.changeStockButton.place(x = 250, y = 587)

        self.addItemButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Add Item', hover_color=cc.lightPurple, command = self.addItem)
        self.addItemButton.place(x = 515, y = 587)

    def exit(self):

        masterMaster = self.master.master
        self.master.destroy()
        ItemDetails(masterMaster).place(x = 0, y = 0)

    def addItem(self):

        sql = "insert into item(request_units_used, storage_units_used, current_stock, item_name, pantry_ID) values (%s, %s, 'Medium', %s, %s)"
        
        units = self.itemUnitsVar.get()
        itemName = self.itemName.get()
        
        mycursor.execute(sql, (units, units, itemName, PANTRY_ID))
        mydb.commit()

    def changeItemStock(self):

        sql = "update item set current_stock = %s where item_name = %s"

        stock = self.stockLevelVar.get()
        itemName = self.itemNameVar.get()

        print(stock, itemName)

        mycursor.execute(sql, (stock, itemName))
        mydb.commit()

class AddItemBatches(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)

        self.master = master
        
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Pantry\AddItemBatches.png'),
                                                  dark_image=Image.open(r'images\Pantry\AddItemBatches.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        stockLevels = ['Low','Medium','High']
        self.stockLevelVar = customtkinter.StringVar()

        itemUnits = ['g / grams', 'kg / kilograms']
        self.itemUnitsVar = customtkinter.StringVar()

        mycursor.execute("select item_name from item")
        items = mycursor.fetchall()

        itemNames = []
        for item in items:
            itemNames.append(item[0])

        self.itemNameVar = customtkinter.StringVar()
        self.itemNameVar1 = customtkinter.StringVar()

        self.itemName = customtkinter.CTkComboBox(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white', values = itemNames, variable = self.itemNameVar)
        self.itemName.place(x=218, y=153)

        self.batchNo = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.batchNo.place(x=632, y=153)

        self.quantity = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.quantity.place(x=218, y=215)

        self.expiry = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.expiry.place(x=632, y=215)

        self.itemName1 = customtkinter.CTkComboBox(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white', values = itemNames, variable = self.itemNameVar1)
        self.itemName1.place(x=218, y=398)

        self.batchNo1 = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.batchNo1.place(x=632, y=398)

        self.exitButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple, command = self.exit)
        self.exitButton.place(x = 385, y = 587)

        self.changeStockButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Delete Batch', hover_color=cc.lightPurple, command = self.deleteItemBatches)
        self.changeStockButton.place(x = 250, y = 587)

        self.addItemButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Add/Change Batch', hover_color=cc.lightPurple, command = self.addBatch)
        self.addItemButton.place(x = 515, y = 587)

    def exit(self):

        masterMaster = self.master.master
        self.master.destroy()
        ItemDetails(masterMaster).place(x = 0, y = 0)

    def addBatch(self):

        global PANTRY_ID

        batchNo = self.batchNo.get()
        itemName = self.itemNameVar.get()
        quantity = self.quantity.get()

        date_ = self.expiry.get()
        date_ = datetime.strptime(date_, '%d-%m-%Y').date()

        mycursor.execute("SELECT item_ID FROM item WHERE item_name = %s", (itemName,))
        itemID = mycursor.fetchall()[0][0]

        sql = "select * from pantryitembatches where batch_no = %s and item_ID = %s"
        mycursor.execute(sql, (batchNo,itemID))
        result = mycursor.fetchall()

        if(len(result)):

            sql = "update pantryitembatches set quantity = %s where batch_no = %s and item_ID = %s"
            mycursor.execute(sql, (quantity, batchNo, itemID))
            mydb.commit()

        else:

            sql = "insert into pantryitembatches (item_ID, batch_no, expiry_date, quantity, pantry_ID) VALUES(%s,%s, %s, %s,%s)"
            mycursor.execute(sql, (itemID, batchNo, date_, quantity, PANTRY_ID))
            mydb.commit()

    def deleteItemBatches(self):

        sql = "delete from pantryitembatches where batch_no = %s and item_ID = %s"

        batchNo = self.batchNo1.get()
        itemName = self.itemNameVar1.get()

        mycursor.execute("SELECT item_ID FROM item WHERE item_name = %s", (itemName,))
        itemID = mycursor.fetchall()[0][0]

        mycursor.execute(sql, (batchNo, itemID))
        mydb.commit()


class EmployeeEntry(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675)
        
        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Pantry\EmployeeEntryPage.png'),
                                                  dark_image=Image.open(r'images\Pantry\EmployeeEntryPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        self.nameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.nameField.place(x=219, y=162)

        self.pnumberField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.pnumberField.place(x=219, y=222)

        self.emailIDField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.emailIDField.place(x=219, y=286)

        self.addressField = customtkinter.CTkTextbox(self, width=171, height=120, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.addressField.place(x=219, y=356)

        self.rationField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.rationField.place(x=219, y=507)

        self.pantryIDField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.pantryIDField.place(x=219, y=575)

        self.usernameField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.usernameField.place(x=669, y=158)

        self.passwordField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.passwordField.place(x=669, y=213)

        self.repeatPasswordField = customtkinter.CTkEntry(self, width=171, height=28, corner_radius=12, fg_color='white', border_width=1, border_color='gray', bg_color='white')
        self.repeatPasswordField.place(x=669, y=268)

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 530, y = 400)

        signUpButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Sign Up', hover_color=cc.lightPurple, command = self.signUp)
        signUpButton.place(x = 702, y = 400)

    def signUp(self):

        errors = []

        name = self.nameField.get()
        pnumber = self.pnumberField.get()
        address = self.addressField.get(1.0, "end-1c")
        email = self.emailIDField.get()
        rationNumber = self.rationField.get()

        username = self.usernameField.get()
        password = self.passwordField.get()
        repeatPassword = self.repeatPasswordField.get()
        pantryID = self.pantryIDField.get()

        mycursor.execute("SELECT username from pantrymanager")
        unavailableUsernames = mycursor.fetchall()

        for unavailableUsername in unavailableUsernames:
            if(unavailableUsername[0] == username):
                errors.append("Unavailable Username")

        if(name == '' or
           pnumber == '' or
           address == '' or
           email == '' or
           rationNumber == '' or
           username == '' or
           password == ''): 
            errors.append("All fields are mandatory")

        if(is_integer(pnumber) != True): errors.append("Phone number must be an integer")
        if(is_integer(rationNumber) != True): errors.append("Ration number must be an integer")

        if(len(pnumber) != 10): errors.append("Phone number must be 10 digits")
        if(len(rationNumber) != 10): errors.append("Ration number must be 10 digits")

        if(password != repeatPassword): errors.append("Password and repeat password don't match")

        mycursor.execute("SELECT * FROM Pantries")
        pantries = mycursor.fetchall()

        if(pantryID != ''):
            present = False
            for row in pantries:
                if(row[0] == int(pantryID) and pantryID != ''):
                    present = True
            
            if(present == False): errors.append("Invalid Pantry ID")

        if(len(errors) > 0):
            Error(self, errors)
            return

        sql = "insert into pantrymanager(username, password, ration_card_number, name, phone_number, email_id, Address, pantry_ID) values (%s,%s, %s, %s, %s, %s, %s,%s)"
        values = (username, password, rationNumber, name, pnumber, email, address, pantryID)

        mycursor.execute(sql, values)
        mydb.commit()


# MAIN CLASS #####################

class FeedFirstPantryManager(customtkinter.CTk):

    def __init__(self):

        customtkinter.CTk.__init__(self)
        self.geometry('900x675')
        self.title('FeedFirstPantryManager')

        LogIn(self).place(x = 0, y = 0)


# MAIN FUNCTION #####################

def main():

    FF = FeedFirstPantryManager()
    FF.mainloop()

    mycursor.close()
    mydb.close()

if __name__ == '__main__':
    main()