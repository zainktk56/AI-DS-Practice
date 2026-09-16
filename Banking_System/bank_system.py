import random

acc_database = [] 

def open_account(account_title, cnic, account_deposit):
    account = {
        "account_title": account_title,
        "cnic": cnic,
        "account_deposit": account_deposit,
        "account_number": random.randint(10000, 99999),
        "account_pin": random.randint(1000, 9999),
    }
    return account

while True:
    print("\n=== WELCOME TO THE BANK ===")
    print("1. Open New Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")
    
    choice = int(input("Select an option (1-4): "))
    
    if choice == 1:
        title_input = input("Enter Account Title : ")
        cnic_input = int(input("Enter your CNIC : "))
        deposit_input = int(input("Enter Deposit Amount : "))
        new_account = open_account(title_input, cnic_input, deposit_input)
        acc_database.append(new_account)
        print(f"\nAccount Created Successfully!")
        print(f"Account Number: {new_account['account_number']}")
        print(f"PIN: {new_account['account_pin']}")
        
    elif choice == 2:
        
        search_input = int(input("Enter Account Number: ")) 
        for account in acc_database:
            if account["account_number"] == search_input:
                pin_number = int(input("Enter your PIN: "))
                if account["account_pin"] == pin_number:
                    print(f"Your Current Balance is : {account['account_deposit']}")
                else:
                    print("Invalid Pin")
                break
        else:
            print("Account Not Found!")
    
    elif choice==3:
        search_input=int(input("Enter Account Number: ")) 
        for account in acc_database:
                    if account["account_number"] == search_input:
                        pin_number = int(input("Enter your PIN: "))
                        if account["account_pin"] == pin_number:
                            amount_deposit=int(input("Enter the Deposit Amount : "))
                            account['account_deposit']=account['account_deposit']+amount_deposit
                            
                            print(f"Deposit Sucessfull !\n Current Balance : {account['account_deposit']} ")
                        else:
                            print("Invalid Pin")
                        break
        else:
            print("Account Not Found!")
      
    elif choice==4:
            search_input=int(input("Enter Account Number: ")) 
            for account in acc_database:
                        if account["account_number"] == search_input:
                            pin_number = int(input("Enter your PIN: "))
                            if account["account_pin"] == pin_number:
                                amount_withdraw=int(input("Enter the Withdrawl Amount : "))
                                account['account_deposit']=account['account_deposit']-amount_withdraw
                                
                                print(f"Withdrawl Sucessfull !\n Current Balance After Withd21rawl : {account['account_deposit']} ")
                            else:
                                print("Invalid Pin")
                            break
            else:
                print("Account Not Found!")        
                
            
    elif choice == 5:
        print("Thank you for banking with us!")
        break
