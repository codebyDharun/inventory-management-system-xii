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