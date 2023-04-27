import sqlite3
import sys

def createAccount():
    try:
        connection = sqlite3.connect("Workbase.db")
    
    except:
        print("Connection does not work")
        sys.exit()
        
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user WHERE UserID != -1")
    userlist = cursor.fetchall()
    i = 0
    for x in userlist:#increments i to make new unique id
        i++
    
    print("Welcome to account creation\n")
    
    fname = input("Please enter your first name\n")
    lname = input("Please enter your last name\n")
    password = input("Please enter password\n")
    bil = input("Please enter your billing address\n")
    ship = input("Please enter your shipping address\n")
    dob = input("Please enter your date of birth\n")
    cnum = input("Please enter your credit or debit card number\n")
    csv = input("Please enter your card security number\n")
    
    
    cursor.execute("INSERT INTO user (UserId, FirstName, LastName, Password, BillingAddress, ShippingAddress, DateOfBirth, CardNumber, SecurityNumber) VALUES(?,?,?,?,?,?,?,?,?)", (i, fname, lname,Password,bil,ship,dob,cnum,csv))
    connection.commit()
    print("Account created\n")
    cursor.close()
    connection.close()
    return i #returns UserId
