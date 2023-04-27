import sqlite3
import sys
try:
    connection = sqlite3.connect("Workbase.db")

except:
    print("Connection does not work")
    sys.exit()
cursor = connection.cursor()

class Account:
    def __init__(self, userID):
        self.userID = userID
    def __delete__(self, userID):#deletes from memoery, not database
        del self.userID
    
    def accInfo(self):
        cursor.execute(f"SELECT * FROM user WHERE UserId={self.userID}")
        userlist = cursor.fetchall()
        for x in userlist:
            print("User ID": x[0])
            print("First name:", x[1])
            print("Last Name:", x[2])
            print("Password:", x[3])
            print("Billing Address:", x[4])
            print("Shipping Address:", x[5])
            print("Date of birth:", x[6])
            print("Card number:", x[7])
            print("Security code:", x[8])
            
        return True
    
    
    
    def Accdel(self):#deletes account in database, not memory
        cursor.execute("DELETE FROM user WHERE UserId=?", (self.userID))
        connection.commit()
        return True
        
    def editname(self):
        newfname = input("What is your updated first name? \n")
        newlname = input("What is your updated last name? \n")
        cursor.execute("UPDATE user SET FirstName=? WHERE UserId=?", (newfname, self.userID))
        cursor.execute("UPDATE user SET LastName=? WHERE UserId=?", (newlname, self.userID))
        connection.commit()
        return True
        
    def editdob(self):
        newdob = input("What is your updated date of birth \n")
        cursor.execute("UPDATE user SET DateOfBirth=? WHERE UserId=?", (newdob, self.userID))
        connection.commit()
        return True
    
    def editpass(self):
        newpass = input("What is your updated password \n")
        cursor.execute("UPDATE user SET Password=? WHERE UserId=?", (newpass, self.userID))
        connection.commit()
        return True
        
    def editship(self):
        newship = input("What is your new shipping address? \n")
        cursor.execute("UPDATE user SET ShippingAddress=? WHERE UserId=?", (newship, self.userID))
        connection.commit()
        return True
    
    def editbill(self):
        newship = input("What is your new billing address? \n")
        cursor.execute("UPDATE user SET BillingAddress=? WHERE UserId=?", (newship, self.userID))
        connection.commit()
        return True
        
    def editpay(self):
        newcnum = input("What is your new credit or debit card number? \n")
        newcsv = input("What is your new card's security number? \n")
        cursor.execute("UPDATE user SET CardNumber=? WHERE UserId=?", (newcnum, self.userID))
        cursor.execute("UPDATE user SET SecurityNumber=? WHERE UserId=?", (newcsv, self.userID))
        connection.commit()
        return True
        
