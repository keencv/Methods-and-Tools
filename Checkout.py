import sqlite3
import sys
try:
    connection = sqlite3.connect("Workbase.db")

    print("It works")

except:
    print("Connection does not work")

    
    sys.exit()
cursor = connection.cursor()

## where it only views the current login persons cart
def viewcheckout(Mainid):
    cursor.execute(f"SELECT * FROM cart WHERE UserId={Mainid}")
    records = cursor.fetchall()

    for x in records:
       ##funny copied code
        print("ItemId:", x[1])
        print("ItemName:", x[2])
        print("ItemDescription:", x[3])
        print("ItemQuantity:", x[4])
        print("ItemCost:", x[5])
        print("\n")

nume = 312
viewcheckout(nume)
cursor.close()
connection.close()