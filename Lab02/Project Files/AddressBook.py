import re

class AddressBook:
    def __init__(self, filename):
        self.filename = filename
        self.list = self.readData(self.filename)

    def parseDict(self,d):
        dictionary = dict()
        # Removes curly braces and splits the pairs into a list
        pairs = d.strip('{}').split(', ')
        for i in pairs:
            pair = i.split(': ')
            # Other symbols from the key-value pair should be stripped.
            dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
        return dictionary


    def readData(self,filename):
        try:
            templist = list()
            dictionary = dict()
            file = open(filename, 'r')
            lines = file.read().split('\n')
            for l in lines:
                if l != '':
                    dictionary = self.parseDict(l)
                    templist.append(dictionary)
            file.close()
            return templist
        except:
            print("Exception occurred!")

    def viewControls(self):
        choice = 0
        while(choice!=8):
            print("What do you want to do with AddressBook?\n1. Add contact in Address Book\n2. Exact Search Contact by following :\n\t Name (first name , last name), Mobile, Phone, City, Email, Website.\n3. Special Search By:\n\t Name (first name , last name), Mobile, Phone, City, Email, Website.\n4. Delete contact By:\n\t name , mobile and phone.\n5. Delete all contacts By:\n\t name , city and mobile.\n6. Update Contact in Address Book.\n7: View All Contacts\n8: Exit.")
            choice = int(input("Enter Choice(1-8): "))
            self.validateChoice(choice,8)
            if(choice==1):
                self.addContactRecord()
            if (choice == 2):
                self.exactSearch()
            if (choice == 3):
                self.specialSearch()
            if (choice == 4):
                self.deleteBy()
            if (choice == 5):
                self.deleteAllBy()
            if (choice == 6):
                self.updateRecord()
            if (choice == 7):
                self.viewAll()
            if (choice == 8):
                ch = int(input("Save Changes? 1: Yes\t2: No\nEnter Choice:? "))
                self.validateChoice(ch,2)
                if(ch==1):
                    self.saveData()


    def validateName(self, name):
        regex = "^[a-zA-Z-]+ +[a-zA-Z-]"
        while not re.search(regex,name):
            name = input("Invalid Input String must only contain alphabets...\n Enter Name: ")

    def validateMobile(self, mobile):
        while (len(mobile) != 12) or (mobile[4]!='-'):
            mobile = input("Invalid Input String must contain '-' and 11 numbers...\n Enter Mobile: ")

    def validateEmail(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+@[a-z0-9-]+.[a-z.]+$"
        while not re.search(regex, email):  # email.find("@") is False or email.find(".") is False:
            email = input("Invalid Input String must contain '@' and '.'...\n Enter Email: ")

    def validateWebsite(self, website):
        while not (website.startswith("www.")) or not (website.find(".")):
            website = input("Invalid Input String must start with 'www.' and contain '.'...\n Enter Website: ")

    def validateChoice(self,choice,range):
        while choice > range:
            choice = int(input("invalid input choice must not be greater than "+ str(range) + "\nEnter Choice(1-"+str(range)+')?'))

    def printContact(self, rec):
        key = list(rec.keys())
        val = list(rec.values())
        for x in range(len(key)):
            print(key[x] + ": " + val[x], end="\t,\t")
        print('\n')


    def viewAll(self):
        for x in self.list:
            self.printContact(x)

    def addContactRecord(self):
        name = input("Enter Name: ")
        self.validateName(name)
        mobile = input("Enter Mobile: ")
        self.validateMobile(mobile)
        phone = int(input("Enter Phone: "))
        email = input("Enter Email: ")
        self.validateEmail(email)
        website = input("Enter Website: ")
        self.validateWebsite(website)
        city = input("Enter City: ")
        contact = {"Name": name, "Mobile": mobile, "Phone": str(phone), "Email": email, "Website": website, "City": city}
        self.list.append(contact)
        print("operation successful...")

    def exactSearch(self):
        choice = 0
        while choice != 7:
            print("Exact Search by?\n1: Name\t2: Mobile\t3: Phone\n4: City\t5: Email\t6: Website\n7: Back to Menu")
            choice = int(input("Enter Choice(1-7)? : "))
            self.validateChoice(choice,7)
            if (choice == 1):
                print("Search by?\n1: First Name\t2: Last Name")
                ch = int(input("Enter Choice(1-2)? : "))
                self.validateChoice(ch, 2)
                if (ch == 1):
                    name = input("Enter First Name: ")
                    regex = "^[a-zA-Z-]"
                    while not re.search(regex, name):
                        name = input("Invalid Input String must only contain alphabets...\n Enter First Name: ")
                    for x in self.list:
                        record = dict(x)
                        ln = record.get("Name").split(' ')
                        if (ln[0] == name):
                            self.printContact(record)
                if (ch == 2):
                    name = input("Enter Last Name: ")
                    regex = "^[a-zA-Z-]"
                    while not re.search(regex, name):
                        name = input(
                            "Invalid Input String must only contain alphabets...\n Enter Last Name: ")
                    for x in self.list:
                        record = dict(x)
                        ln = record.get("Name").split(' ')
                        if (ln[1] == name):
                            self.printContact(x)
            if (choice == 2):
                mobile = input("Enter Mobile: ")
                self.validateMobile(mobile)
                for x in self.list:
                    record = dict(x)
                    m = record.get("Mobile")
                    if (m == mobile):
                        self.printContact(x)
            if (choice == 3):
                phone = int(input("Enter Phone: "))
                for x in self.list:
                    record = dict(x)
                    p = record.get("Phone")
                    if (p == phone):
                        self.printContact(x)
            if (choice == 4):
                city = input("Enter City: ")
                for x in self.list:
                    record = dict(x)
                    c = record.get("City")
                    if (c == city):
                        self.printContact(x)
            if (choice == 5):
                email = input("Enter email: ")
                self.validateEmail(email)
                for x in self.list:
                    record = dict(x)
                    e = record.get("Email")
                    if (e == email):
                        self.printContact(x)
            if (choice == 6):
                website = input("Enter Website: ")
                self.validateWebsite(website)
                for x in self.list:
                    record = dict(x)
                    w = record.get("Website")
                    if (w == website):
                        self.printContact(x)

    def specialSearch(self):
        choice = 0
        while choice != 7:
            print("Exact Search by?\n1: Name\t2: Mobile\t3: Phone\n4: City\t5: Email\t6: Website\n7: Back to Menu")
            choice = int(input("Enter Choice(1-6)? : "))
            self.validateChoice(choice,7)
            if (choice == 1):
                print("Search by?\n1: First Name\t2: Last Name")
                ch = int(input("Enter Choice(1/2)? : "))
                self.validateChoice(ch,2)
                if (ch == 1):
                    name = input("Enter First Name: ")
                    for x in self.list:
                        record = dict(x)
                        n = record.get("Name").split(' ')
                        if (n[0].find(name) != -1):
                            self.printContact(x)
                if (ch == 2):
                    name = input("Enter Last Name: ")
                    for x in self.list:
                        record = dict(x)
                        n = record.get("Name").split(' ')
                        if (n[1].find(name) != -1):
                            self.printContact(x)
            if (choice == 2):
                mobile = input("Enter Mobile: ")
                for x in self.list:
                    record = dict(x)
                    m = record.get("Mobile")
                    if (m.find(mobile) != -1):
                        self.printContact(x)
            if (choice == 3):
                phone = (input("Enter Phone: "))
                for x in self.list:
                    record = dict(x)
                    p = (record.get("Phone"))
                    if (p.find(phone) != -1):
                        self.printContact(x)
            if (choice == 4):
                email = input("Enter email: ")
                for x in self.list:
                    record = dict(x)
                    e = record.get("Email")
                    if (e.find(email) != -1):
                        self.printContact(x)
            if (choice == 5):
                website = input("Enter Website: ")
                for x in self.list:
                    record = dict(x)
                    w = record.get("Website")
                    if (w.find(website) != -1):
                        self.printContact(x)
            if (choice == 6):
                city = input("Enter City: ")
                for x in self.list:
                    record = dict(x)
                    c = record.get("City")
                    if (c.find(city) != -1):
                        self.printContact(x)

    def saveData(self):
        try:
            file = open(self.filename, "w")
            for i in self.list:
                file.write(str(i) + '\n')
            print("Data Updated Successfully...")
            file.close()
        except:
            print("Exception occurred!")

    def deleteBy(self):
        print("Delete by?\n1: Name\t2: Mobile\t3: Phone")
        choice = int(input("Enter Choice(1-3)? : "))
        if (choice == 1):
            name = input("Enter Name:? ")
            self.validateName(name)
            for x in self.list:
                record = dict(x)
                n = record.get("Name")
                if (n == name):
                    self.list.remove(x)
                    print("operation successful...")
                    return
        if (choice == 2):
            mobile = input("Enter Mobile: ")
            self.validateMobile(mobile)
            for x in self.list:
                record = dict(x)
                m = record.get("Mobile")
                if (m == mobile):
                    self.list.remove(x)
                    print("operation successful...")
                    return
        if (choice == 3):
            phone = input("Enter Phone: ")
            for x in self.list:
                record = dict(x)
                p = record.get("Phone")
                if (p == phone):
                    self.list.remove(x)
                    print("operation successful...")
                    return

    def deleteAllBy(self):
        print("Delete by?\n1: Name\t2: Mobile\t3: Phone")
        choice = int(input("Enter Choice(1-3)? : "))
        if (choice == 1):
            name = input("Enter Name:? ")
            self.validateName(name)
            for x in self.list:
                record = dict(x)
                n = record.get("Name")
                if (n == name):
                    self.list.remove(x)
        if (choice == 2):
            mobile = input("Enter Mobile: ")
            self.validateMobile(mobile)
            for x in self.list:
                record = dict(x)
                m = record.get("Mobile")
                if (m == mobile):
                    self.list.remove(x)
        if (choice == 3):
            phone = input("Enter Phone: ")
            for x in self.list:
                record = dict(x)
                p = record.get("Phone")
                if (p == phone):
                    self.list.remove(x)

    def updateRecord(self):
        i = 0
        for i in range(len(self.list)):
            print(i,' - ',end='\t')
            self.printContact(self.list[i])
        index = int(input("Enter Number of Record You want to update(0-"+str(i)+')? '))
        self.validateChoice(index,i)
        rec = self.list[index]
        print("What do You want to Update?\n1: Name\t2: Mobile\t3: Phone\n4: Email\t5: Website\t6: City")
        choice = int(input("Enter Choice(1-6)? : "))
        self.validateChoice(choice, 6)
        if (choice == 1):
            name = input("Enter Name: ")
            self.validateName(name)
            rec.update({"Name":name})
        if (choice == 2):
            mobile = input("Enter Mobile: ")
            self.validateMobile(mobile)
            rec.update({"Mobile":mobile})
        if (choice == 3):
            phone = int(input("Enter Phone: "))
            rec.update({"Phone":phone})
        if (choice == 4):
            email = input("Enter Email: ")
            self.validateEmail(email)
            rec.update({"Email":email})
        if (choice == 5):
            website = input("Enter Website: ")
            self.validateWebsite(website)
            rec.update({"Website":website})
        if (choice == 6):
            city = input("Enter City: ")
            rec.update({"City":city})