#Creating the Mini Bank ohhh yeah!
amount=0
def main():
    print("Welcome to the most efficient bank!!!")
    print("1)Login\n2)Create Account\n3)Exit")
    while True:
        a=getnum()
        match a:
                case 1:
                    log()
                    print("Account Locked!!,press 3 to exit:",end="")
                case 3:
                    print("Exited..")
                    exit()
                case _:
                    print("Try again!!,Just login other features are under construction..")
                    
def log():
    i=3
    while i>0:
        x=input("Enter username:")
        y=input("Enter Pass: ")
        if x=="max60" and y=="1234":
            print("1)Check Balance\n2)Widthdraw\n3)Deposite\n4)Transfer Money\n5)Exit")
            while True:
                x=getnum()
                match x:
                    case 1:
                        balance()
                    case 2:
                        Widthdraw()
                    case 3:
                        deposite()
                    case 4:
                        transfer()
                    case 5:
                        print("Exited..")
                        exit()
                    case _:
                        print("Invalid Input!!")
        else:
            print(f"Invalid pass or username!!{i} tries remaining")
            i-=1
def balance():
     print(f"Your current balance is Rs.{amount:,}")

def deposite():
   print("Enter the amount: ")
   global amount
   amount+=getnum()
   print("Deposited successfully")

def transfer():
    print("Enter the amount: ")
    global amount
    enter_amt=getnum()
    if (enter_amt<=amount):
        amount-=enter_amt
        print("Transferred successfully")
    else:
        print("Insufficient Balance")

def Widthdraw():
    print("Enter the amount: ")
    global amount
    enter_amt=getnum()
    if (enter_amt<=amount):
        amount-=enter_amt
        print("Widthdrawed successfully")
    else:
        print("Insufficient Balance")

def getnum():
    while True:
        try:
            y=int(input("-->"))
        except:
            print("Try again!")
        else:
            return y
main()

