USE FeedFirst;

-- SET FOREIGN_KEY_CHECKS = 0;  

CREATE TABLE Item (
    item_ID INT AUTO_INCREMENT PRIMARY KEY,
    request_units_used VARCHAR(30),
    storage_units_used VARCHAR(30),
    current_stock VARCHAR(30),
    item_name VARCHAR(30)
);

CREATE TABLE PantryItemBatches (
    item_ID INT,
    batch_ID INT AUTO_INCREMENT PRIMARY KEY,
    batch_no INT,
    expiry_date DATE,
    quantity INT,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID)
);

create table Pantries(
	pantry_ID INT AUTO_INCREMENT PRIMARY KEY,
	pantry_name VARCHAR(20),
	pantry_address VARCHAR(120));

create table PantryManager(
	username VARCHAR(20),
	password VARCHAR(20),
	employee_ID INT AUTO_INCREMENT PRIMARY KEY,
	ration_card_number VARCHAR(10),
	name VARCHAR(20),
	phone_number VARCHAR(10),
	email_ID VARCHAR(50),
	address VARCHAR(150),
	pantry_ID INT,
	FOREIGN KEY(pantry_ID) REFERENCES Pantries(pantry_ID)
);

-- FoodVouchers, PantryItemBatches, and Item must be connected to pantries
create table Recipients(
	recipient_ID INT AUTO_INCREMENT PRIMARY KEY,
	phone_number INT,
	name VARCHAR(20),
	ration_card_number INT,
	username VARCHAR(20),
	password VARCHAR(20),
	household_member_names VARCHAR(150),
	email_ID VARCHAR(20),
	dietary_needs VARCHAR(120),
	household_size INT,
	pantry_ID INT,
	address VARCHAR(120),
	priority VARCHAR(20),
	FOREIGN KEY(pantry_ID) REFERENCES Pantries(pantry_ID)
);

create table FoodVouchers(
	recipient_ID INT,
	FOREIGN KEY(recipient_ID) REFERENCES Recipients(recipient_ID),
	voucher_ID INT AUTO_INCREMENT PRIMARY KEY, 
	status VARCHAR(20)
);

CREATE TABLE RequestedItem (
    item_ID INT,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    voucher_ID INT,
    FOREIGN KEY (voucher_ID) REFERENCES FoodVouchers(voucher_ID),
    requested_quantity INT,
    provided_quantity INT
);