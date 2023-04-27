import sqlite3
import sys

def createAccount():#returns true or false
    try:
        connection = sqlite3.connect("Workbase.db")
    
    except:
        print("Connection does not work")
        sys.exit()
        
    cursor = connection.cursor()
    userinput = input("What is your User ID? \n")
    cursor.execute(f"SELECT * FROM user WHERE UserID ={userinput}")
    userlist = cursor.fetchall()
    for x in userlist:
        passwordinput = input("What is your password? \n")
        if (passwordinput = x[3]):
            print("Logged in\n")
            return True
        else:
            print("Incorrect user ID or password\n")
            return False
            
        
