CREATE TABLE user(
UserId int,
FirstName varchar(25),
LastName varchar(25),
Password varchar(25),
BillingAddress varchar(55),
ShippingAddress varchar(55),
DateOfBirth varchar(25),
CardNumber varchar(35),
SecurityNumber varchar(25),
PRIMARY KEY(UserId)
);

CREATE TABLE inventory(
ItemId int,
ItemName varchar(25),
ItemDescription varchar(25),
ItemQuantity int,
ItemCost float,
PRIMARY KEY(ItemId)
);

--I need the foreign key
CREATE TABLE cart(
UserId int,
ItemId int,
ItemName varchar(25),
ItemDescription varchar(25),
ItemQuantity int,
ItemCost float,
FOREIGN KEY(UserId)
REFERENCES user(UserId)
);

--got to have primary key^
--Forign key here to keep track of history
CREATE TABLE orderhistory(
UserId int,
ItemId int,
ItemName varchar(25),
ItemDescription varchar(25),
ItemQuantity int,
ItemCost float,
FOREIGN KEY(UserId)
REFERENCES user(UserId)
)
--Or just a foreign key works