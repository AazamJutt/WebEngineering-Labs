import pymysql

#Task 2
class Product:
    def __init__(self,product_id,product_title,product_des,product_units,product_price):
        self.product_id = product_id
        self.product_title = product_title
        self.product_des = product_des
        self.product_units = product_units
        self.product_price = product_price

#utility functions
def createProduct():
    id = input("Enter Product's Info\n ID:? ")
    title = input("Title:? ")
    des = input("Description:? ")
    unit = input("Units:? ")
    price = input("Price:? ")
    product = Product(id,title,des,unit,price)
    return product

def displayAll():
    # create db connection
    db = None
    cursor = None
    try:
        # create db connection
        db = pymysql.connect(host='localhost', user='root', password='versatile', database='mydb')
        # Create cursor object
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = "Select * from products"
        cursor.execute(query)
        results = cursor.fetchall()
        for r in results:
            print(r)
    except Exception as e:
        print("Error connecting db", str(e))
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()

#Task3            
def insertProduct(product):
    # create db connection
    db = None
    cursor = None
    try:
        # create db connection
        db = pymysql.connect(host='localhost', user='root', password='versatile', database='mydb')
        # Create cursor object
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = "insert into products values(%s,%s,%s,%s,%s)"
        args = (product.product_id,product.product_title,product.product_des,product.product_units,product.product_price)
        cursor.execute(query,args)
        db.commit()
    except Exception as e:
        print("Error connecting db", str(e))
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()
            print("record(s) inserted successfully...")
            

#Task5
def fetch_wrt_units(units):
    # create db connection
    db = None
    cursor = None
    try:
        # create db connection
        db = pymysql.connect(host='localhost', user='root', password='versatile', database='mydb')
        # Create cursor object
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = "Select * from products where product_units<%s"
        args = (units)
        cursor.execute(query, args)
        results = cursor.fetchall()
    except Exception as e:
        print("Error connecting db", str(e))
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()
            return results

        
#Task6
def deleteProduct(product_id):
    # create db connection
    db = None
    cursor = None
    try:
        # create db connection
        db = pymysql.connect(host='localhost', user='root', password='versatile', database='mydb')
        # Create cursor object
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = "delete from products where product_id = %s"
        args = (product_id)
        cursor.execute(query, args)
        db.commit()
    except Exception as e:
        print("Error connecting db", str(e))
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


print("Records in DB are: ")
displayAll()
res = deleteProduct(4)
print("\nRemaining records after deleting product with id=4: ")
displayAll()
