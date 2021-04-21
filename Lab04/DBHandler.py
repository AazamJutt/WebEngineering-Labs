import pymysql
import re


# Task 2
class DBHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def validateRoll(self, roll):
        pattern = r'^[bBmM][cCsSiI][sSeEtT][fFsS]\d\d[mMaA]\d\d\d$'
        return re.search(pattern, roll)

    def validateEmail(self, email):
        pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z]+.[a-zA-Z]+$"
        return re.search(pattern, email)

    def validatePhone(self, phone):
        pattern = r"^\d\d\d\d-\d\d\d\d\d\d\d$"
        return re.search(pattern, phone)

    def addStudent(self, roll, name, phone, email, cgpa):
        cursor = None
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            if (self.validateRoll(roll) != True or self.validateEmail(email) != True or self.validatePhone(
                    phone != True)):
                print('Operation Failed...')
                return False
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            query = f"INSERT INTO students(roll,name,phone,email,cgpa) values('{roll}', '{name}','{phone}','{email}','{cgpa}')"
            args = (roll, name, phone, email, cgpa)
            cursor.execute(query, args)
            connection.commit()
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
            print('Record(s) added succesfully...')
            return True

    def updateStudent(self, roll, new_name, new_phone, new_email, new_cgpa):
        cursor = None
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            if (self.validateRoll(roll) is not True or self.validateEmail(new_email) is not True or self.validatePhone(
                    new_phone is not True)):
                print('hello')
                return False
            cursor = connection.cursor(pymysql.cursors)
            query = f"UPDATE `students` SET `name`='{new_name}', `phone`='{new_phone}', `email`='{new_email}', `cgpa`='{new_cgpa}' WHERE roll = {roll}"
            # args = (new_name, new_phone, new_email, new_cgpa, roll)
            cursor.execute(query)
            connection.commit()
            print('done')
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
            return True

    def deleteStudent(self, roll):
        cursor = None
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            if self.validateRoll(roll):
                return False
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            query = f"DELETE FROM students WHERE roll = '{roll}'"
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
            return True

    def getStudentsByName(self):
        cursor = None
        results = None
        student = {}
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            query = "Select * from students order by name desc"
            cursor.execute(query)
            results = cursor.fetchall()
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
            return results

    def isStudent(self, roll):
        cursor = None
        result = None
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            query = "Select * from students where roll=%s"
            cursor.execute(query, roll)
            result = cursor.fetchone()
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
            if result is not None:
                return True
            else:
                return False

    def getStudentData(self, roll):
        cursor = None
        student = {}
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            query = "Select roll,name,phone,email,cgpa from students where roll=%s"
            cursor.execute(query, roll)
            results = cursor.fetchall()
            for r in results:
                val = r.values()
                val = list(val)
                student.update(roll=val[0])
                student.update(name=val[1])
                student.update(phone=val[2])
                student.update(email=val[3])
                degree = None
                course = None
                year = None
                session = None
                section = None
                campus = None
                roll_no = None
                if roll[0] == 'B':
                    degree = "Bachelors"
                else:
                    defree = "Masters"
                student.update(degree=degree)
                if (roll[1:3] == 'CS'):
                    course = 'Computer Science'
                if (roll[1:3] == 'SE'):
                    course = 'Software Engineering'
                if (roll[1:3] == 'IT'):
                    course = 'Information Technology'
                student.update(course=course)
                year = roll[4:6]
                student.update(year=year)
                session = '20' + roll[4:6]
                student.update(session=session)
                if (roll[6] == '5' or roll[6] == '0'):
                    campus = 'Old'
                else:
                    campus = 'New'
                student.update(campus=campus)
                student.update(roll_no=roll[8:10])
                student.update(cgpa=val[4])
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
            return student

    def getHighestCGPA(self):
        student = {}
        try:
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            query = "Select roll, email, cgpa from students where cgpa = (select max(cgpa) from students)"
            cursor.execute(query)
            results = cursor.fetchall()
            for r in results:
                val = r.values()
                val = list(val)
                student.update(roll=val[0])
                student.update(email=val[1])
                student.update(cgpa=val[2])
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
            return student

    def displayAll(self):
        # create db connection
        cursor = None
        try:
            # create db connection
            connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            # Create cursor object
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            query = "Select * from students"
            cursor.execute(query)
            results = cursor.fetchall()
            for r in results:
                print(r)
        except Exception as e:
            print("Error connecting db", str(e))
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
