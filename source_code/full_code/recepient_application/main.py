import customtkinter
from PIL import Image
from extrakinter import widget_move
from extrakinter import lengthen_widget_downwards
import math
import mysql.connector

from utils.widgets import FrameLeave, Error
from utils.functions import is_integer

from modules.pantryEntity import Pantry

import constants.colour_constants as cc

import os

from dotenv import load_dotenv

from modules.log_in import LogIn

### ENVIRONMENT VARIABLES ###############

load_dotenv()

### SQL CONNECTION ######################

mydb = mysql.connector.connect(
  host="localhost",
  user=os.getenv("FF_USERNAME"),
  password=os.getenv("FF_PASSWORD"),
  database="FeedFirst"
)

mycursor = mydb.cursor()

# USERNAME VARIABLE #######################
        
global USERNAME
global USER_RECEPIENT_ID

# SPECIAL CLASSES #########################

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

### PAGE CLASSES #############################

class FoodVoucher(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width = 900, height = 675)

        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Recepient\VoucherPage.png'),
                                                  dark_image=Image.open(r'images\Recepient\VoucherPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):


        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 530, y = 580)

        #customerSupportButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Voucher Records', hover_color=cc.lightPurple)
        #customerSupportButton.place(x = 140, y = 512)

        voucherRecordButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Voucher Records', hover_color=cc.lightPurple, command = self.voucherDetails)
        voucherRecordButton.place(x = 140, y = 572)

        itemsAndUnitsButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Items and Units', hover_color=cc.lightPurple, command = self.itemsAndUnits)
        itemsAndUnitsButton.place(x = 140, y = 178)

        applyButton = customtkinter.CTkButton(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Apply for Voucher', hover_color=cc.lightPurple, command = self.applyVoucher)
        applyButton.place(x = 690, y = 580)

        itemAndQuantityFrame = customtkinter.CTkScrollableFrame(self, width = 344, height = 412, fg_color='white', bg_color='white')
        itemAndQuantityFrame.place(x = 503, y = 141)

        self.itemNames = []
        self.itemIDs = []
        mycursor.execute("select pantry_ID from recepients WHERE username = %s", (USERNAME,))
        data = mycursor.fetchall()
        pantry_ID = data[0][0]

        mycursor.execute("select * from item where pantry_ID = %s", (pantry_ID,))

        items = mycursor.fetchall()
        for item in items:
            self.itemNames.append(item[4])
            self.itemIDs.append(item[0])
        
        mydb.commit()
        
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
        for i in range(0,16,1):
            if(i%2==0):
                customtkinter.CTkLabel(itemAndQuantityFrame, width = 140, height = 38, anchor = 'e', text = 'Item ' + str(j+1) + ':         ').grid(row = i, column = 0)
                customtkinter.CTkComboBox(itemAndQuantityFrame, width = 180, height = 30, variable = self.itemVars[j], values=self.itemNames).grid(row = i, column = 1)
                j+=1
            else:
                customtkinter.CTkLabel(itemAndQuantityFrame, width = 140, height = 38, anchor = 'e', text = 'Quantity ' + str(j) + ' :         ').grid(row = i, column = 0)
                customtkinter.CTkEntry(itemAndQuantityFrame, width = 180, height = 30, textvariable= self.quantityVars[k]).grid(row = i, column = 1)
                k+=1
            

    def voucherDetails(self):

        voucherDetails = VoucherDetails(self)
        voucherDetails.place(x = 0, y = 0)

    def itemsAndUnits(self):

        ItemDetails(self).place(x = 0, y = 0)

    def applyVoucher(self):

        global USER_RECEPIENT_ID

        errors = []

        mycursor.execute('SELECT pantry_ID FROM recepients WHERE recepient_id = %s',(USER_RECEPIENT_ID,))
        data = mycursor.fetchall()
        pantry_ID = data[0][0]

        sql = 'INSERT INTO foodvouchers(recepient_id, status,pantry_ID) values (%s,"PENDING",%s)'

        mycursor.execute(sql,(USER_RECEPIENT_ID,pantry_ID))
        mydb.commit()

        last_inserted_id = mycursor.lastrowid

        sql = 'INSERT INTO requesteditem(item_ID, voucher_ID, requested_quantity) VALUES(%s, %s, %s)'

        for i in range(0, 8, 1):
            item = self.itemVars[i].get()
            if (item not in self.itemNames) and (item != ''):
                errors.append("Invalid items entered")
                break
            elif ((self.quantityVars[i].get().isnumeric() != True) and (self.quantityVars[i].get() != '')):
                errors.append("Only numerical values to be entered as quantities")
                break
            elif item != '':
                    item_id = self.itemIDs[self.itemNames.index(item)]
                    voucher_id = last_inserted_id
                    requested_quantity = self.quantityVars[i].get()
                    
                    values = (item_id, voucher_id, requested_quantity)
                    
                    mycursor.execute(sql, values)
        
        mydb.commit()

        if(len(errors) > 0):
            Error(self, errors)
            

class VoucherDetails(customtkinter.CTkFrame):

    def __init__(self, master):

        customtkinter.CTkFrame.__init__(self, master, width=900, height=675, bg_color='white')

        self.setBackground()
        self.placeWidgets()

    def setBackground(self):

        background_image = customtkinter.CTkImage(light_image=Image.open(r'images\Recepient\VoucherDetailsPage.png'),
                                                  dark_image=Image.open(r'images\Recepient\VoucherDetailsPage.png'),
                                                  size=(900, 675))
        
        background_label = customtkinter.CTkLabel(self, image=background_image, text='')
        background_label.pack()

    def placeWidgets(self):

        global USER_RECEPIENT_ID

        self.itemNames = []
        self.itemIDs = []
        
        mycursor.execute("select pantry_ID from recepients WHERE username = %s", (USERNAME,))
        data = mycursor.fetchall()
        pantry_ID = data[0][0]

        mycursor.execute("select * from item where pantry_ID = %s", (pantry_ID,))

        items = mycursor.fetchall()
        for item in items:
            self.itemNames.append(item[4])
            self.itemIDs.append(item[0])

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 385, y = 595)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 800, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 30, y = 180)

        sql = "SELECT voucher_id FROM foodvouchers WHERE recepient_id = %s"
        mycursor.execute(sql, (USER_RECEPIENT_ID,))

        voucher_IDs = mycursor.fetchall()

        i = 0
        for voucher_ID in voucher_IDs:

            sql = "SELECT status FROM foodvouchers WHERE voucher_id = %s"
            mycursor.execute(sql, voucher_ID)
            status = mycursor.fetchall()

            sql = "SELECT * FROM requesteditem WHERE voucher_id = %s"
            mycursor.execute(sql, voucher_ID)
            items = mycursor.fetchall()
            itemsNamesDisplay = [] 
            requestedQuantities = []
            providedQuantities = []
            for item in items:
                itemsNamesDisplay.append(self.itemNames[self.itemIDs.index(item[0])])
                requestedQuantities.append(item[2])
                providedQuantities.append(item[3])

            VoucherRecord(listFrame, voucher_ID[0],itemsNamesDisplay,requestedQuantities,itemsNamesDisplay,providedQuantities, status[0][0]).grid(row = i, column = 0)
            i+=1

        mydb.commit()


class VoucherRecord(customtkinter.CTkFrame):

    def __init__(self, master, ID, requestedItemList, requestedQuantityList, providedItemList, providedQuantityList,status):

        customtkinter.CTkFrame.__init__(self, master, width = 782, height = 262, fg_color='white', border_color='pink', border_width=1, corner_radius=0)

        self.placeDetails(ID, requestedItemList, requestedQuantityList, providedItemList, providedQuantityList, status)

    def placeDetails(self, ID, requestedItemList, requestedQuantityList, providedItemList, providedQuantityList, status):

        voucherID = customtkinter.CTkLabel(self, width = 178, height = 30, fg_color='white', text = ID, anchor='center')
        voucherID.place(x = 5, y = 10)

        yi = 30
        y = 10
        for i in range(0, len(requestedItemList), 1):
            customtkinter.CTkLabel(self, width = 215, height = 30, fg_color='white', text = str(requestedItemList[i]) + " - " + str(requestedQuantityList[i]), anchor='center').place(x = 181, y = y)
            y+=yi

        y = 10
        for i in range(0, len(providedItemList), 1):
            customtkinter.CTkLabel(self, width = 215, height = 30, fg_color='white', text = str(providedItemList[i]) + " - " + str(providedQuantityList[i]), anchor='center').place(x = 405, y = y)
            y+=yi

        statusID = customtkinter.CTkLabel(self, width = 164, height = 30, fg_color='white', text = status, anchor='center')
        statusID.place(x = 614, y = 10)

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

        exitButton = FrameLeave(self, width = 120, height = 42, corner_radius=20, border_width=0, bg_color='white', fg_color=cc.darkPurple,text_color='white', text='Exit', hover_color=cc.lightPurple)
        exitButton.place(x = 385, y = 587)

        listFrame = customtkinter.CTkScrollableFrame(self,width = 775, height = 390, fg_color='white', bg_color='white')
        listFrame.place(x = 57, y = 180)

        mycursor.execute("select pantry_ID from recepients WHERE username = %s", (USERNAME,))
        data = mycursor.fetchall()
        pantry_ID = data[0][0]

        mycursor.execute("select * from item where pantry_ID = %s", (pantry_ID,))
        items = mycursor.fetchall()

        i = 0
        for item in items:
            ItemAndUnitsRecord(listFrame, item[4], item[3], item[1]).grid(column = 0, row = i)
            i+=1

        mydb.commit()

### MAIN CLASS ###################################

class FeedFirstRecepient(customtkinter.CTk):

    def __init__(self):

        customtkinter.CTk.__init__(self)
        self.geometry('900x675')
        self.title('FeedFirstRecepient')
        #customtkinter.CTkFrame(self, width = 900, height = 675, corner_radius = 0, bg_color = cc.lightPink, fg_color= lightPink).place(x = 0, y = 0)

        #slideUp(self, LogIn(self))
        LogIn(self).place(x = 0, y = 0)

### MAIN FUNCTION ################################

def main():

    FF = FeedFirstRecepient()
    FF.mainloop()

    mycursor.close()
    mydb.close()


if __name__ == '__main__':
    main()
