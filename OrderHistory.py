import sqlite3
import datetime
con = sqlite3.connect("Workbase.db")
cur = con.cursor()

class OrderHistory:
    def __init__(self, userID):
        self.userID = userID

    def addOrderToHistory(self):
        x = datetime.datetime.now()
        date = x.strftime("%c")
        cur.execute(f"SELECT * FROM cart WHERE UserId ={self.userID}")
        cart = cur.fetchall()
        
        for row in cart:
            itemId = row[1]
            itemName = row[2]
            itemDescription = row[3]
            itemQuantity = row[4]
            itemCost = row[5]
            cur.execute("INSERT INTO orderhistory (UserID, ItemId, ItemName, ItemDescription, ItemQuantity, ItemCost, DateOrdered) VALUES (?,?,?,?,?,?,?)", (self.userID, itemId, itemName, itemDescription, itemQuantity, itemCost, date))
            con.commit()
        return True

    def viewOrderHistory(self):
        cur.execute(f"SELECT * FROM orderhistory WHERE UserId ={self.userID}")
        history = cur.fetchall()

        for row in history:
            print("ItemId: ", row[1])
            print("ItemName: ", row[2])
            print("ItemDescription: ", row[3])
            print("ItemQuanity: ", row[4])
            print("ItemCost: ", row[5])
            print("OrderDate: ", row[6])
            print("\n")

    def deleteHistory(self):
        cur.execute(f"DELETE FROM orderhistory WHERE UserId ={self.userID}")
        con.commit()
        return True

