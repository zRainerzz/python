balance=0

def main():
    print(f"Balance: {balance}")
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")

def deposit(n):
    global balance
    #global is needed to inform python that balance is not a local variable,that's not a bug, that's meant for you to edit this variable up above.
    balance +=n
    #shortcut for balance=balance+n

def withdraw(n):
    global balance
    balance -=n
    

if __name__ =="__main__":
    main()