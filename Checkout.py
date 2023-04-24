import sqlite3
import sys
try:
    connection = sqlite3.connect("Workbase.db")

    print("It works")

except:
    print("Connection does not work")

    
    sys.exit()
cursor = connection.cursor()







cursor.close()
connection.close()