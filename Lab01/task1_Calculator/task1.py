import math
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def percentage(obtained,total):
    if(obtained>total):
        return 'invalid input'
    return (obtained*100)/total
def factorial(n):
    if(n<0):
        return 'invalid input'
    return math.factorial(n)
def ln(n):
    return math.log(n,math.e)
def log(n):
    return math.log(n,10)
def sqrt(n):
    return math.sqrt(n)
def pow(a,b):
    return math.pow(a,b)
def sin(n):
    return math.sin(n)
def sininverse(n):
    if (n<-1 or n>1):
        return 'invalid input'
    return math.asin(n)
def cos(n):
    if (n<-1 or n>1):
        return 'invalid input'
    return math.cos(n)
def cosinverse(n):
    return math.acos(n)
def tan(n):
    return math.tan(n)
def taninverse(n):
    return math.atan(n)
choice = 1
print("1:  ADD\n2:  SUBTRACT\n3:  DIVIDE\n4:  MULTIPLE\n5:  PERCENTAGE\n6:  FACTORIAL\n7:  NATURAL LOG\n8:  LOG\n9:  SQRT\n10: POWER\n11: SIN\n12: SIN INVERSE\n13: COS\n14: COS INVERSE\n15: TAN\n16: TAN INVERSE\n17: EXIT\n")
while(choice != 17):
    choice = int(input("Enter choice? "))
    if(choice>=1 and choice<=4):
        a = float(input("Enter number A: "))
        b = float(input("Enter number B: "))
        if(choice==1):
            print("Result: ",sum(a,b))
        if(choice==2):
            print("Result: ",sub(a,b))
        if(choice==3):
            print("Result: ",div(a,b))
        if(choice==4):
            print("Result: ",mul(a,b))
    if(choice==5):
        a = float(input("Enter Obtained: "))
        b = float(input("Enter Total: "))
        print("Result",percentage(a,b))
    if(choice>=6 and choice<17 and choice!=10):
        a = float(input("Enter number N: "))
        if (choice == 6):
            print("Result: ",factorial(a))
        if (choice == 7):
            print("Result: ",ln(a))
        if (choice == 8):
            print("Result: ",log(a))
        if (choice == 9):
            print("Result: ",sqrt(a))
        if (choice == 11):
            print("Result: ", sin(a))
        if (choice == 12):
            print("Result: ", sininverse(a))
        if (choice == 13):
            print("Result: ", cos(a))
        if (choice == 14):
            print("Result: ", cosinverse(a))
        if (choice == 15):
            print("Result: ", tan(a))
        if (choice == 16):
            print("Result: ", taninverse(a))
    if(choice==10):
        a = float(input("Enter N: "))
        b = float(input("Enter power: "))
        print("Result: ", pow(a,b))
    input("Press ENTER key to continue...")
    print('\n')
