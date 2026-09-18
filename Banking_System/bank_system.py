import random

acc_database = []

def open_account(account_title, cnic, account_deposit):
    return {
        "account_title": account_title,
        "cnic": cnic,
        "account_deposit": account_deposit,
        "account_number": random.randint(10000, 99999),
        "account_pin": random.randint(1000, 9999),
    }

def find_account(account_number, pin=None):
    for account in acc_database:
        if account["account_number"] == account_number:
            if pin is not None and account["account_pin"] != pin:
                return "INVALID_PIN"
            return account
    return "NOT_FOUND"

while True:
    print("\n=== WELCOME TO THE BANK ===")
    print("1. Open New Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. Exit")
    
    try:
        choice = int(input("\nSelect an option (1-6): "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    if choice == 1:
        title_input = input("Enter Account Title: ")
        cnic_input = int(input("Enter your CNIC: "))
        deposit_input = int(input("Enter Initial Deposit Amount: "))
        
        new_acc = open_account(title_input, cnic_input, deposit_input)
        acc_database.append(new_acc)
        
        print("\nAccount Created Successfully!")
        print(f"Account Number : {new_acc['account_number']}")
        print(f"PIN            : {new_acc['account_pin']}")

    elif choice == 2:
        acc_num = int(input("Enter Account Number: "))
        pin = int(input("Enter PIN: "))
        
        acc = find_account(acc_num, pin)
        if acc == "INVALID_PIN":
            print("Invalid PIN!")
        elif acc == "NOT_FOUND":
            print("Account Not Found!")
        else:
            print(f"Current Balance: ${acc['account_deposit']}")

    elif choice == 3:
        acc_num = int(input("Enter Account Number: "))
        pin = int(input("Enter PIN: "))
        
        acc = find_account(acc_num, pin)
        if acc == "INVALID_PIN":
            print("Invalid PIN!")
        elif acc == "NOT_FOUND":
            print("Account Not Found!")
        else:
            amount = int(input("Enter Deposit Amount: "))
            if amount > 0:
                acc['account_deposit'] += amount
                print(f"Deposit Successful! New Balance: ${acc['account_deposit']}")
            else:
                print("Invalid deposit amount.")

    elif choice == 4:
        acc_num = int(input("Enter Account Number: "))
        pin = int(input("Enter PIN: "))
        
        acc = find_account(acc_num, pin)
        if acc == "INVALID_PIN":
            print("Invalid PIN!")
        elif acc == "NOT_FOUND":
            print("Account Not Found!")
        else:
            amount = int(input("Enter Withdrawal Amount: "))
            if amount > acc['account_deposit']:
                print("Insufficient Balance!")
            elif amount <= 0:
                print("Invalid amount!")
            else:
                acc['account_deposit'] -= amount
                print(f"Withdrawal Successful! New Balance: ${acc['account_deposit']}")

    elif choice == 5:
        sender_num = int(input("Enter Your Account Number: "))
        sender_pin = int(input("Enter Your PIN: "))
        
        sender = find_account(sender_num, sender_pin)
        if sender == "INVALID_PIN":
            print("Invalid PIN!")
        elif sender == "NOT_FOUND":
            print("Sender Account Not Found!")
        else:
            beneficiary_num = int(input("Enter Beneficiary Account Number: "))
            beneficiary = find_account(beneficiary_num)
            
            if beneficiary in ("NOT_FOUND", "INVALID_PIN"):
                print("Beneficiary Account Not Found!")
            elif beneficiary["account_number"] == sender["account_number"]:
                print("You cannot transfer money to your own account!")
            else:
                confirm = input(f"Transfer to {beneficiary['account_title']}? (Y/N): ").lower()
                if confirm in ('y', 'yes'):
                    amount = int(input("Enter Transfer Amount: "))
                    if amount > sender['account_deposit']:
                        print("Insufficient Balance!")
                    elif amount <= 0:
                        print("Invalid transfer amount!")
                    else:
                        sender['account_deposit'] -= amount
                        beneficiary['account_deposit'] += amount
                        print("\nTransfer Successful!")
                        print(f"Your Remaining Balance: ${sender['account_deposit']}")

    elif choice == 6:
        print("Thank you for banking with us!")
        break
        
    else:
        print("Invalid choice! Please select between 1 and 6.")