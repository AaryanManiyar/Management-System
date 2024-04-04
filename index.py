import os
import mysql.connector
import datetime
now = datetime.datetime.now()

def product_mgmt():
    while True:
        print("1. Add New Product")
        print("2. List Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")
        p = int(input("Enter your Choice: "))
        if p == 1:
            add_product()
        elif p == 2:
            search_product()
        elif p == 3:
            update_product()
        elif p == 4:
            delete_product()
        elif p == 5:
            break

def purchase_mgmt():
    while True:
        print("1. Add Order")
        print("2. List Order")
        print("1. Back to Main Menu")
        o = int(input("Enter your Choice: "))
        if o == 1:
            add_order()
        elif o == 2:
            list_order()
        elif o == 3:
            break   

def sales_mgmt():
    while True:
        print("1. Sale Items")
        print("2. List Sales")
        print("1. Back to Main Menu")
        s = int(input("Enter your Choice: "))
        if s == 1:
            sale_product()
        elif s == 2:
            list_sale()
        elif s == 3:
            break    

def user_mgmt():
    while True:
        print("1. Add User")
        print("2. List User")
        print("1. Back to Main Menu")
        u = int(input("Enter your Choice: "))
        if u == 1:
            add_user()
        elif u == 2:
            list_user()
        elif u == 3:
            break 


def create_database():
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="Maniyar@18", database="Inventory_mgmt")
    mycursor = mydb.cursor()

    print("Creating PRODUCT Table") 
    sql = "CREATE TABLE if not exists product (\p_code int(4), \p_name char(3), \p_price float(8,2), \p_qty int(4), \p_category char(30));"
    mycursor.execute(sql)

    print("Creating ORDER Table")
    sql = "CREATE TABLE if not exists orders (\order_id int(4), \order_date date, \p_code char(30), \p_price float(8,2), \p_qty int(4), \supplier char(50), \p_category char(30));"
    mycursor.execute(sql)

    print("Creating SALES Table")
    sql = "CREATE TABLE if not exists sales (\sales_id int(4), \sales_date date, \p_code char(30), \p_price float(8,2), \p_qty int(4), \Total double(8,2));"
    mycursor.execute(sql)

    print("Creating USERS Table")
    sql = "CREATE TABLE if not exists users (\u_id char(6), \u_name char(30), \u_password char(30));"
    mycursor.execute(sql)

def list_database():
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="Maniyar@18", database="Inventory_mgmt")
    mycursor = mydb.cursor()
    sql = "Show Tables;"
    mycursor.execute(sql)
    for i in mycursor:
        print(i)

def add_order():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Maniyar@18",database="Inventory_mgmt")
    mycursor=mydb.cursor()
    now = datetime.datetime.now()
    sql="INSERT INTO orders(order_id,order_date,p_code,p_price,p_qty,supplier,p_category) values (%s,%s,%s,%s,%s,%s,%s)"
    code=int(input("Enter product code :"))
    o_id=now.year+now.month+now.day+now.hour+now.minute+now.second
    qty=int(input("Enter product quantity : "))
    price=float(input("Enter Product unit price: "))
    category=input("Enter product category: ")
    supplier=input("Enter Supplier details: ")
    val=(o_id,now,code,price,qty,supplier,category)
    mycursor.execute(sql,val)
    mydb.commit()

def list_order():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT * from orders"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t\t ORDER DETAILS")
    print("-"*85)
    print("orderid Date Product code price quantity Supplier Category")
    print("-"*85)
    for i in mycursor:
        print(i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t",i[4],"\t ",i[5],"\t",i[6])
    print("-"*85)
        
def db_mgmt():
    while True:
        print("1. Database Creation")
        print("2. List Database")
        print("1. Back to Main Menu")
        p = int(input("Enter your Choice: "))
        if p == 1:
            create_database()
        elif p == 2:
            list_database()
        elif p == 3:
            break
   
def add_product():
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="Maniyar@18", database="Inventory_Mgmt")
    mycursor = mydb.cursor()
    sql = "INSEERT into product (p_code,p_name,p_price,p_qty,p_category) values (%s,%s,%s,%s,%s)"
    code = int(input("Enter the Product Code: "))
    search = "SELECT COUNT(*) FROM product WHERE p_code = %s;"
    val = (code,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt = x[0]
    if cnt == 0:
        name = input("Enter the Product Name: ")
        qty = int(input("Enter Product Quantity: "))
        price = float(input("Enter Product Unit Price: "))
        category = input("Enter the Product Category: ")
        val = (code,name,price,qty,category)
        mycursor.execute(sql,val)
        mydb.commit()
    else:
        print("Product Already Exists..") 

def update_product():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Maniyar@18",database="Inventory_Mgmt")
    mycursor=mydb.cursor()
    code=int(input("Enter the product code :"))
    qty=int(input("Enter the quantity :"))
    sql="UPDATE product SET p_qty=p_qty+%s WHERE p_code=%s;"
    val=(qty,code)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t\t Product details updated")

def delete_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Maniyar@18",database="Inventory_Mgmt")
    mycursor=mydb.cursor()
    code=int(input("Enter the product code :"))
    sql="DELETE FROM product WHERE p_code = %s;"
    val=(code,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount," record(s) deleted");

def search_product():
    while True :
        print("1. List all product")
        print("2. List product code wise")
        print("3. List product categoty wise")
        print("4. Back (Main Menu)")
        s=int (input("Enter Your Choice :"))
        if s==1 :
            list_product()
        if s==2 :
            code=int(input(" Enter product code :"))
            list_prcode(code)
        if s==3 :
            category=input("Enter category :")
            list_prcat(category)
        if s== 4 :
            break

def list_product():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Maniyar@18",database="Inventory_Mgmt")
    mycursor=mydb.cursor()
    sql="SELECT * from product"
    mycursor.execute(sql)
    print("PRODUCT DETAILS")
    print("","-"*47)
    print("code name price quantity category")
    print("","-"*47)
    for i in mycursor:
        print("",i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t\t",i[4])
    print("","-"*47)

def list_prcode(code):
    mydb=mysql.connector.connect(host="localhost",user="root",password="Maniyar@18",database="Inventory_Mgmt")
    mycursor=mydb.cursor()
    sql="SELECT * from product WHERE p_code=%s"
    val=(code,)
    mycursor.execute(sql,val)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\t\t code name price quantity category")
    print("\t\t","-"*47)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t\t",i[4])
    print("\t\t","-"*47)

def sale_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
    mycursor=mydb.cursor()
    p_code=input("Enter product code: ")
    sql="SELECT count(*) from product WHERE p_code=%s;"
    val=(p_code,)
    mycursor.execute(sql,val)
    for x in mycursor:
        cnt=x[0]
        if cnt !=0 :
            sql="SELECT * from product WHERE p_code=%s;"
            val=(p_code,)
            mycursor.execute(sql,val)
            for x in mycursor:
                print(x)
                price=int(x[2])
                p_qty=int(x[3])
            qty=int(input("Enter no of quantity :"))
            if qty <= p_qty:
                total=qty*price;
                print ("Collect Rs. ", total)
                sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
                val=(int(cnt)+1,datetime.datetime.now(),p_code,price,qty,total)
                mycursor.execute(sql,val)
                sql="UPDATE product SET p_qty=p_qty-%s WHERE p_code=%s"
                val=(qty,p_code)
                mycursor.execute(sql,val)
                mydb.commit()
            else:
                print(" Quantity not Available")
        else:
            print(" Product is not avalaible")

def list_sale():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Maniyar@18",database="Inventory_Mgmt")
    mycursor=mydb.cursor()
    sql="SELECT * FROM sales"
    mycursor.execute(sql)
    clrscr()
    print("SALES DETAILS")
    print("-"*80)
    print("Sales id Date Product Code Price Quantity Total")
    print("-"*80)
    for x in mycursor:
        print(x[0],"\t",x[1],"\t",x[2],"\t ",x[3],"\t\t",x[4],"\t\t",x[5])
    print("-"*80)

def list_prcat(category):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
    mycursor=mydb.cursor()
    print (category)
    sql="SELECT * from product WHERE p_category =%s"
    val=(category,)
    mycursor.execute(sql,val)
    clrscr()
    print("PRODUCT DETAILS")
    print("","-"*47)
    print("code name price quantity category")
    print("","-"*47)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t ",i[3],"\t\t",i[4])
    print("\t\t","-"*47)

def add_user():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Maniyar@18",database="Inventory_Mgmt")
    mycursor=mydb.cursor()
    u_id=input("Enter emaid id :")
    name=input(" Enter Name :")
    paswd=input("Enter Password :")
    sql="INSERT INTO user values (%s,%s,%s);"
    val=(u_id,name,paswd)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, " user created")

def list_user():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="Inventory_Mgmt")
    mycursor=mydb.cursor()
    sql="SELECT uid,uname from users"
    mycursor.execute(sql)
    clrscr()
    print("\t\t\t\t USER DETAILS")
    print("\t\t","-"*27)
    print("\t\t UID name ")
    print("\t\t","-"*27)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1])
    print("\t\t","-"*27)

def clrscr():
    print("\n"*5)

while True:
    clrscr()
    print("\t\t\t STOCK MANAGEMENT")
    print("\t\t\t ****************\n")
    print("\t\t 1. PRODUCT MANAGEMENT")
    print("\t\t 2. PURCHASE MANAGEMENT")
    print("\t\t 3. SALES MANAGEMENT")
    print("\t\t 4. USER MANAGEMENT")
    print("\t\t 5. DATABASE SETUP")
    print("\t\t 6. EXIT\n")
    n=int(input("Enter your choice :"))
    if n== 1:
        product_mgmt()
    if n== 2:
        os.system('cls')
        purchase_mgmt()
    if n== 3:
        sales_mgmt()
    if n== 4:
        user_mgmt()
    if n==5 :
        db_mgmt()
    if n== 6:
        break    