#Project 2
#Create a simple banking system that:
#● Stores customer info in a file
#● Allows deposits and withdrawals using functions
#● Updates customer balance
#● Logs all transactions in a separate file
#● Handles exceptions gracefully
#Files Used:
#customers.txt — stores customer records in the format:
#Name,AccountNumber,Balance
#transactions.txt — appends every deposit or withdrawal record with timestamp

import datetime
try:
    with open("customers.txt", "w") as c:
        c.write("AccountNumber\tName\tBalance\n")
        while True:
            N = input("Enter the name of the customer: ")
            A = input("Enter the account number: ")
            B = int(input("Enter the Balance: "))
            c.write(f"{A}\t{N}\t{B}\n")

            s = input("Do you want to add more (y/n)? ")
            if s.lower() != "y":
                break

except Exception as e:
    print("An error occurred:", e)


def deposit(account_number, amount):
    try:
        with open("customers.txt", "r") as c:
            lines = c.readlines()

        updated = False
        with open("customers.txt", "w") as c:
            for line in lines:
                if line.startswith("AccountNumber"):  # keep header
                    c.write(line)
                    continue
                acc, name, bal = line.strip().split("\t")
                if acc == account_number:
                    bal = str(int(bal) + amount)
                    updated = True
                c.write(f"{acc}\t{name}\t{bal}\n")

        if updated:
            with open("transactions.txt", "a") as t:
                t.write(f"{datetime.datetime.now()} - Deposit {amount} to {account_number}\n")
            print("Deposit successful.")
        else:
            print("Account not found.")

    except Exception as e:
        print("Error in deposit:", e)



def withdraw(account_number, amount):
    try:
        with open("customers.txt", "r") as c:
            lines = c.readlines()

        updated = False
        with open("customers.txt", "w") as c:
            for line in lines:
                if line.startswith("AccountNumber"):  # keep header
                    c.write(line)
                    continue
                acc, name, bal = line.strip().split("\t")
                if acc == account_number:
                    bal_int = int(bal)
                    if bal_int >= amount:
                        bal = str(bal_int - amount)
                        updated = True
                    else:
                        print("Insufficient balance.")
                c.write(f"{acc}\t{name}\t{bal}\n")

        if updated:
            with open("transactions.txt", "a") as t:
                t.write(f"{datetime.datetime.now()} - Withdraw {amount} from {account_number}\n")
            print("Withdrawal successful.")

    except Exception as e:
        print("Error in withdrawal:", e)
        

    

        

