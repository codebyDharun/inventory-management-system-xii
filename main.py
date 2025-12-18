#imported modules 
import datetime
import mysql.connector

#verfication of mysql connection 

def checking():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="project",database="inventory_db")
        mycursor=mydb.cursor()
        mycursor.execute("use inventory_db")
        mydb.commit()
        mycursor.execute("CREATE TABLE IF NOT EXISTS Products (id INT PRIMARY KEY,name VARCHAR(255),price INT,quantity INT)")
        mydb.commit()
        mycursor.execute("INSERT IGNORE INTO Products VALUES(1, 'Samsung', 20000, 10),(2, 'iPhone', 80000, 12),(3, 'Oppo', 15000, 15),(4, 'Xiaomi', 10000, 20),(5, 'Vivo', 17000, 17)")
        mydb.commit()
        mycursor.close()
    except mysql.connector.Error as err:
        mydb=mysql.connector.connect(host="localhost",user="root",password="project")
        mycursor=mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS inventory_db")
        mydb.commit()
        mycursor.execute("use inventory_db")
        mydb.commit()
        mycursor.execute("CREATE TABLE IF NOT EXISTS Products (id INT PRIMARY KEY,name VARCHAR(255),price INT,quantity INT)")
        mydb.commit()
        mycursor.execute("INSERT INTO Products VALUES (1, 'Samsung', 20000, 10),(2, 'iPhone', 80000, 12),(3, 'Oppo', 15000, 15),(4, 'Xiaomi', 10000, 20),(5, 'Vivo', 17000, 17)")
        mydb.commit()
        mycursor.close()
    finally:
        integrated()

def integrated():
    global mydb
    global mycursor
    mydb=mysql.connector.connect(host="localhost",user="root",password="project",database="inventory_db")
    mycursor=mydb.cursor()


# Main program functions 
def user_interface():
    while True:
        Banner()
        ch = int(input("Enter choice: "))

        if ch == 1:
            Show_all()
        
        elif ch == 2:
            Add_Product()

        elif ch == 3:
            Update_Quantity()
        
        elif ch == 4:
            Price()
        
        elif ch == 5:
            Sales()

        elif ch == 6:
            Delete()

        elif ch == 7:
            print("Have a Nice Day :)")
            mycursor.close()
        else:   
            print("wrong input!!!")
            
def Show_all():

    print("---------------INVENTORY---------------")
    mycursor.execute("SELECT * FROM Products")
    allproducts = mycursor.fetchall()
    if allproducts !=None:
        for records in allproducts:
            print(records)
    else:
        print("No products found in inventory.")

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

def Sales():  # fixed version
    Show_all()
    try:
        id_no = int(input("Enter product ID number sold: "))
        sold_qty = int(input("Enter quantity sold: "))
        mycursor.execute("SELECT name, price, quantity FROM Products WHERE id = {0}".format(id_no))
        product = mycursor.fetchone()
        if product is None:
            print("Product not Found")
            return

        name, price, current_qty = product

        if sold_qty <= current_qty:
            new_qty = current_qty - sold_qty
            upd_val = "UPDATE Products SET quantity = {0} WHERE id = {1}".format(new_qty, id_no)
            mycursor.execute(upd_val)
            mydb.commit()
            total = price * sold_qty
            print("Sale recorded successfully.")
            print("\n--- Bill ---")
            print("Mobiles Warehouse, Inc.")
            print("Date:", datetime.datetime.now().strftime("%d-%m-%Y"))
            print("Time:", datetime.datetime.now().strftime("%H:%M:%S"))
            print("Item:", name)
            print("Qty:", sold_qty)
            print("Total: ₹", total)
            print("Thank you!")
        else:
            print("Insufficient stock.", current_qty, "only available")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

    except Exception as e:
        print("Error:", e)

def Delete():
    Show_all()
    try:
        d = int(input("Enter the Product id you want to delete:"))
        ele=mycursor.execute("DELETE FROM ProductS WHERE id = {0}".format(d))
        print("Deleted Successfully")
    except ValueError:
        print("Invalid input!")
    finally:
        user_interface()

#Banners
def Banner():

    print("\n===================================\n   WELCOME TO MOBILES WAREHOUSE    \n===================================")
    print("\n-----------------MENU-----------------")
    print("\t1. Show Products")
    print("\t2. Add product")
    print("\t3. Update quantity")
    print("\t4. Change price")
    print("\t5. Sales")
    print("\t6. Delete product")
    print("\t7. Quit")
    print("----------------------------------------")

checking()
user_interface()