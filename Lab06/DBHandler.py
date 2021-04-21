import  pymysql
from Donor import Donor
from  User import User
import re


class DBHandler:
    def __init__(self , dbipaddress,dbuser,dbpwd,dbname):
        self.dbipaddress=dbipaddress
        self.dbuser=dbuser
        self.dbpwd=dbpwd
        self.dbname=dbname

    def vaildateName(self,name):
        if name is None:
            return False
        if(len(name)>20):
            return False
        return True

    def validateEmail(self, email):
        pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z]+.[a-zA-Z]+$"
        return re.search(pattern, email)

    def validatePhone(self,phone):
        pattern = r"^\d{4}-\d{7}$"
        return re.search(pattern, phone)

    def validateCNIC(self, cnic):
        pattern = r"^\d{5}-\d{7}-\d$"
        return re.search(pattern, cnic)

    def validateBG(self, bg):
        pattern = r"^A\+|O\+|B\+|AB|A-|O-|B-|AB-$"
        return re.search(pattern, bg)

    def vaildateCity(self, name):
        if name is None:
            return False
        if(len(name)>50):
            return False
        return True

    def insertUser(self, user):
        print(user.name+user.email+user.password)
        db = None
        cursor = None
        insert= False
        if not self.vaildateName(user.name) or not self.validateEmail(user.email):
            return insert
        else:
            try:
                db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
                cursor = db.cursor(pymysql.cursors.DictCursor)
                query = "insert into users(username,email,password) values(%s,%s,%s)"
                args = (user.name,user.email,user.password)
                cursor.execute(query, args)
                db.commit()
                insert=True
            except Exception as e:
                print("Exception occured")
                print(e)
            finally:
                if cursor != None:
                    cursor.close()
                if db != None:
                    db.close()
                return insert


    def verifyUser(self,user):
        db = None
        cursor = None
        verified= False
        if not self.validateEmail(user.email):
            return verified
        else:
            try:
                db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
                cursor = db.cursor(pymysql.cursors.DictCursor)
                query = "select username,password from users where email=%s"
                cursor.execute(query, user.email)
                password = ""
                if cursor is not None:
                    res = cursor.fetchall()
                    print(res[0])
                    user.name = res[0]["username"]
                    password = res[0]["password"]
                if password==user.password:
                    verified=True
                    return verified
            except Exception as e:
                print("Exception occured")
            finally:
                if cursor != None:
                    cursor.close()
                if db != None:
                    db.close()
                return verified

    def insertDonor(self , donor):
        db = None
        cursor = None
        insert= False
        if(self.vaildateName(donor.name) is False or self.validatePhone(donor.phone) is False or self.validateCNIC(donor.cnic) is False or self.validateBG(donor.blood_group) is False or self.vaildateCity(donor.city)is False):
            return insert
        else:
            try:
                db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
                cursor = db.cursor(pymysql.cursors.DictCursor)
                query = "insert into donors(name,blood_group,phone,cnic,city) values(%s,%s,%s,%s,%s)"
                args = (donor.name,donor.blood_group,donor.phone,donor.cnic,donor.city)
                cursor.execute(query, args)
                db.commit()
                insert=True
            except Exception as e:
                print("Exception occured")
                print(e)
            finally:
                if cursor != None:
                    cursor.close()
                if db != None:
                    db.close()
                return insert


    def getAvailableDonors(self,blood_group):
        db = None
        cursor = None
        donorList = []
        try:
            # create db connection
            # db = pymysql.connect("localhost","root","m@vra123","test")
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            # Create cursor object
            cursor = db.cursor(pymysql.cursors.DictCursor)
            # args=(1)
            query = "select * from donors where blood_group = %s"
            cursor.execute(query,blood_group)
            results = cursor.fetchall()
            print("return type", type(results))
            print(results)

            for r in results:
                donorList.append(Donor(r["name"],r["blood_group"],r["phone"],r["cnic"],r["city"]))

        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return donorList


    def fetchAllDonors(self):
        # create db connection
        db = None
        cursor = None
        donorList = []
        try:
            # create db connection
            # db = pymysql.connect("localhost","root","m@vra123","test")
            db = pymysql.connect(host=self.dbipaddress, user=self.dbuser, password=self.dbpwd, database=self.dbname)
            # Create cursor object
            cursor = db.cursor(pymysql.cursors.DictCursor)
            query = "Select name,blood_group,phone,cnic,city from donors"
            # args=(1)
            cursor.execute(query)
            results = cursor.fetchall()
            print("return type", type(results))
            print(results)

            for r in results:
                donorList.append(Donor(r["name"],r["blood_group"],r["phone"],r["cnic"],r["city"]))
                #print("id", r["id"], "rollno", r["rollno"], "semmester", r["semmester"])

        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor != None:
                cursor.close()
            if db != None:
                db.close()
            return donorList