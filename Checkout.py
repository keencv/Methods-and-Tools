import sqlite3
import sys
try:
    connection = sqlite3.connect("Workbase.db")

   ## print("It works")

except:
    print("Connection does not work")

    
    sys.exit()
cursor = connection.cursor()
## where it only views the current login persons cart
def viewchart(Mainid):
    cursor.execute(f"SELECT * FROM cart WHERE UserId={Mainid}")
    records = cursor.fetchall()

    for x in records:
       ##funny copied code
        print("ItemId:", x[1])
        print("ItemName:", x[2])
        print("ItemDescription:", x[3])
        print("ItemQuantity:", x[4])
        ItemQuantity1 = x[4]
        print("ItemCost:", x[5])
       ##Stupid workaround
        ItemCost = x[5]
        ItemCost = ItemCost * ItemQuantity1
        print(ItemCost)
        print("\n")
def AddToCart(UserId):
    Name1 = input("Enter item name\n")
    Itemcou1 = input("Enter item count\n")
    cursor.execute(f"SELECT * FROM inventory WHERE ItemName='{Name1}'")
    records = cursor.fetchall()
    for x in records:
        ##funny copied code
        ItemId = x[0]
        ItemName = x[1]
        ItemDescription = x[2]
        ItemQuantity = x[3]
        ItemCost = x[4]

        cursor.execute("INSERT INTO cart (UserId, ItemId, ItemName, ItemDescription, ItemQuantity, ItemCost) VALUES(?,?,?,?,?,?)", (UserId, ItemId, ItemName,ItemDescription,Itemcou1,ItemCost))
        connection.commit()
def DeleteFromCart(UserId):
    Name1 = input("Enter item name\n")
    Itemcou1 = input("Enter item count\n")
##Why would anyone put the same thing into the cart more than once
    cursor.execute("DELETE FROM cart WHERE ItemName=? AND ItemQuantity=? AND UserId=?", (Name1,Itemcou1,UserId,))
    connection.commit()

def CheckoutFromCart(UserId):
    cursor.execute(f"SELECT * FROM cart WHERE UserId={UserId}")
    records = cursor.fetchall()
    for x in records:
        ##funny copied code
        UserId = x[0]
        ItemId = x[1]
        ItemName = x[2]
        ItemDescription = x[3]
        ItemQuantity1 = x[4]
       # print("ItemQuantity:", x[4])
        ItemCost = x[5]
        cursor.execute(f"SELECT * FROM inventory WHERE ItemId={ItemId}")
        info = cursor.fetchall()
        for y in info:
            ##funny copied code
            ItemQuantity2 = y[3]
          #  print("ItemQuantity:", y[3])


        ItemQuantityM = ItemQuantity2 - ItemQuantity1
        ItemCost = ItemCost * ItemQuantity1
        ##cursor.execute( "INSERT INTO orderhistory (UserId, ItemId, ItemName, ItemDescription, ItemQuantity, ItemCost) VALUES(?,?,?,?,?,?)", (UserId, ItemId, ItemName, ItemDescription, ItemQuantity1, ItemCost))
        cursor.execute("DELETE FROM cart WHERE ItemName=? AND ItemQuantity=? AND UserId=?", (ItemName, ItemQuantity1, UserId,))
        cursor.execute("UPDATE inventory SET ItemQuantity=? WHERE ItemId=?", (ItemQuantityM, ItemId))
        connection.commit()

def DeleteFromCartAccountDelete(UserId):
##Why would anyone put the same thing into the cart more than once
    cursor.execute("DELETE FROM cart WHERE UserId=?", (UserId,))
    connection.commit()

##nume = 312
##AddToCart(nume)
##DeleteFromCartAccountDelete(nume)
cursor.close()
connection.close()