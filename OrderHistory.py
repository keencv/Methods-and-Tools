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

# Just a test I made to make sure each function works
"""
def main():
    userId = 1
    currentUser = OrderHistory(userId)
    print("Welcome!\nEnter your choice below...")
    while 1:
        print("1. View your order history\n2. Add order to history from cart\n3. Delete your order history\n4. Exit")
        a = int(input("Enter your choice: "))
        print("")
        if a == 1:
            print("Here are your past orders: \n")
            currentUser.viewOrderHistory()
        elif a == 2:
            if currentUser.addOrderToHistory() == True:
                print("Your order has been added to your history!\n")
            else:
                print("Failed to add order. Try again...\n")
        elif a == 3:
            if currentUser.deleteHistory() == True:
                print("Your order history has been deleted.\n")
            else:
                print("Failed to delete order history. Try again...\n")
        elif a == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid response try again...\n")
main()
"""