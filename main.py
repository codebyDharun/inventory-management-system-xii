#---------------INVENTORY---MANAGEMENT---SYSTEM---------------

#MODULES IMPORTED

import random
import datetime
import mysql.connector

#INTEGRATED DATABASE CONNECTION SETUP

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="150309", database="inventory_db")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE Products(id INT PRIMARY KEY, name VARCHAR(255), price INT, quantity INT)")
except mysql.connector.errors.ProgrammingError as e:
    print("Database table already exists, No worries!")
    
#USER-DEFINED FUNCTIONS
#1
def Banner():

    print("\n===================================")
    print("   WELCOME TO MOBILES WAREHOUSE    ")
    print("===================================")
#2
def header():

    print("\n-----------------MENU-----------------")
    print("\t1. Show Products")
    print("\t2. Search price/quantity")
    print("\t3. Add product")
    print("\t4. Update quantity")
    print("\t5. Change price")
    print("\t6. Sales")
    print("\t7. Delete product")
    print("\t8. Quit")
    print("-------------------------------------")
#3
def Show_all():

    print("---------------INVENTORY---------------")
    mycursor.execute("SELECT * FROM Products")
    allproducts = mycursor.fetchall()
    if allproducts !=None:
        print("ID | Name     | Price | Qty")
        for product in allproducts:
            print(product[0], " | ", product[1], " | ₹", product[2], " | ", product[3])
    else:
        print("No products found in inventory.")
#4
def Search():

    Show_all()

    try:
        search_id=int(input("Enter the product no. to change the Price/Quantity:"))
        mycursor.execute("SELECT * FROM Product WHERE id = {0}".format(search_id))
        s=mycursor.fetchone()
        print(s)
    except ValueError:
        print("Enter correct values!")  
#5
def Add_Product():

    id_no = int(input("Enter Product ID number: "))
    p_name = input("Enter Product name: ")
    price = int(input("Enter Product price: "))
    quantity = int(input("Enter Product quantity: "))
    ins_val = "INSERT INTO Products VALUES ({0}, '{1}', {2}, {3})".format(id_no, p_name, price, quantity)
    mycursor.execute(ins_val)
    mydb.commit()

    Show_all()

    print("Product added successfully.")
#6
def Update_Quantity():

    Show_all()

    try:
        id_no = int(input("Enter product ID number to update quantity: "))
        new_qty = int(input("Enter new quantity: "))
        upd_val = "UPDATE Products SET quantity = {0} WHERE id = {1}".format(new_qty, id_no)
        mycursor.execute(upd_val)
        mydb.commit()
        print("Quantity updated successfully.")
    except:
        print("Error updating quantity.")
#7
def Price():

    Show_all()

    try:
        id_no = int(input("Enter product ID number to change price: "))
        new_price = int(input("Enter new price: "))
        upd_val = "UPDATE Products SET price = {0} WHERE id = {1}".format(new_price, id_no)
        mycursor.execute(upd_val)
        mydb.commit()
        print("Price updated successfully.")
    except:
        print("Error updating price.")
#8
def Sales():

    Show_all()

    try:
        id_no = int(input("Enter product ID number sold: "))
        sold_qty = int(input("Enter quantity sold: "))
        mycursor.execute("SELECT quantity FROM Products WHERE id = {0}".format(id_no))
        product = mycursor.fetchone()
        if product is None:
            print("Product not Found")
            return
        name,price,current_qty=product
        if sold_qty <= current_qty:
            new_qty = current_qty - sold_qty
            upd_val = "UPDATE Products SET quantity = {0} WHERE id = {1}".format(new_qty, id_no)
            mycursor.execute(upd_val)
            mydb.commit()
            total = price * sold_qty
            print("Sale recorded successfully.")
            print("\n--- Bill ---")
            print("Mobiles Warehouse, Inc.")
            print("Bill No:", int(random.random()*100000))
            print("Date:", datetime.datetime.now().strftime("%d-%m-%Y"))
            print("Time:", datetime.datetime.now().strftime("%H:%M:%S"))
            print("Item:", name)
            print("Qty:", sold_qty)
            print("Total: ₹", total)
            print("Thank you!")
        else:
            print("Insufficient stock.",current_qty,"only available")
    except ValueError:
        print("Invalid input.")
    except mysql.connector.Error as err:
        print("Database Error")
    except Exception as e:
        print("Error processing sale:",e)
#9
def Delete():

    Show_all()

    try:
        d = int(input("Enter the Product id you want to delete:"))
        ele=mycursor.execute("DELETE FROM Product WHERE id = {0}").format(d)
        print(ele,"Deleted Successfully")
    except ValueError:
        print("Invalid input!")

y = True
while y:

    Banner()
    header()

    try:
        ch = int(input("Enter choice: "))
    
    except:
        ch = 0
    
    if ch == 1:
        Show_all()
    
    elif ch == 2:
        Search()
    
    elif ch == 3:
        Add_Product()

    elif ch == 4:
        Update_Quantity()
    
    elif ch == 5:
        Price()
    
    elif ch == 6:
        Sales()

    elif ch == 7:
        Delete()

    elif ch == 8:
        print("Have a Nice Day :)")
    else:   
        print("Functionality not yet implemented.")
        break


    

