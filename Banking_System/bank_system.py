import streamlit as str
import random

# Initialize session state for database to keep it alive across refreshes
if "acc_database" not in str.session_state:
    str.session_state.acc_database = []

def open_account(account_title, cnic, account_deposit):
    return {
        "account_title": account_title,
        "cnic": cnic,
        "account_deposit": account_deposit,
        "account_number": random.randint(10000, 99999),
        "account_pin": random.randint(1000, 9999),
    }

def find_account(account_number, pin=None):
    for account in str.session_state.acc_database:
        if account["account_number"] == account_number:
            if pin is not None and account["account_pin"] != pin:
                return "INVALID_PIN"
            return account
    return "NOT_FOUND"

def delete_account(account_number, pin=None):
    for index, account in enumerate(str.session_state.acc_database):
        if account["account_number"] == account_number:
            if pin is not None and account["account_pin"] != pin:
                return "INVALID PIN"
            
            remaining_balance = account["account_deposit"]
            str.session_state.acc_database.pop(index)
            return f"ACCOUNT DELETED SUCCESSFULLY! Please withdraw your remaining amount: ${remaining_balance}"
        
    return "ACCOUNT NOT FOUND"

# Streamlit App UI Setup
str.set_page_config(page_title="Core Python Bank System", page_icon="🏦", layout="centered")
str.title("🏦 Core Python Bank System")
str.markdown("---")

# Sidebar navigation menu
menu = [
    "Open New Account", 
    "Check Balance", 
    "Deposit Money", 
    "Withdraw Money", 
    "Transfer Money", 
    "Delete Account",
    "Admin: View All Accounts"
]
choice = str.sidebar.selectbox("Navigate Banking Actions", menu)

if choice == "Open New Account":
    str.subheader("✨ Open a New Banking Account")
    with str.form("open_acc_form", clear_on_submit=True):
        title = str.text_input("Account Title Name")
        cnic = str.text_input("CNIC Number (Numbers Only)")
        deposit = str.number_input("Initial Deposit Amount ($)", min_value=0, step=100)
        submit = str.form_submit_button("Create Account")
        
        if submit:
            if title.strip() == "" or cnic.strip() == "":
                str.error("Please fill out all input fields configuration parameters!")
            else:
                new_user = open_account(title, cnic, deposit)
                str.session_state.acc_database.append(new_user)
                str.success(f"🎉 Account successfully initialized for {title}!")
                str.info(f"💾 **Account Number:** {new_user['account_number']} | 🔑 **PIN:** {new_user['account_pin']}")

elif choice == "Check Balance":
    str.subheader("🔎 Check Account Balance State")
    acc_num = str.number_input("Enter Account Number", min_value=10000, max_value=99999, step=1)
    pin = str.number_input("Enter Account PIN", min_value=1000, max_value=9999, step=1)
    
    if str.button("Fetch Balance"):
        acc = find_account(acc_num, pin)
        if acc == "INVALID_PIN":
            str.error("❌ The PIN code entered is incorrect!")
        elif acc == "NOT_FOUND":
            str.error("❌ No matching active account database record found.")
        else:
            str.success(f"💰 **Current Available Balance:** ${acc['account_deposit']}")

elif choice == "Deposit Money":
    str.subheader("💵 Deposit Funds Matrix")
    acc_num = str.number_input("Enter Account Number", min_value=10000, max_value=99999, step=1)
    pin = str.number_input("Enter Account PIN", min_value=1000, max_value=9999, step=1)
    amount = str.number_input("Enter Amount to Deposit ($)", min_value=1, step=50)
    
    if str.button("Execute Deposit Request"):
        acc = find_account(acc_num, pin)
        if acc == "INVALID_PIN":
            str.error("❌ The PIN code entered is incorrect!")
        elif acc == "NOT_FOUND":
            str.error("❌ No matching active account database record found.")
        else:
            acc['account_deposit'] += amount
            str.success(f"✅ Deposit processed! Your new updated balance state is: ${acc['account_deposit']}")

elif choice == "Withdraw Money":
    str.subheader("🏧 Withdraw Cash Matrix")
    acc_num = str.number_input("Enter Account Number", min_value=10000, max_value=99999, step=1)
    pin = str.number_input("Enter Account PIN", min_value=1000, max_value=9999, step=1)
    amount = str.number_input("Enter Amount to Withdraw ($)", min_value=1, step=50)
    
    if str.button("Execute Withdrawal"):
        acc = find_account(acc_num, pin)
        if acc == "INVALID_PIN":
            str.error("❌ The PIN code entered is incorrect!")
        elif acc == "NOT_FOUND":
            str.error("❌ No matching active account database record found.")
        else:
            if amount > acc['account_deposit']:
                str.error("⚠️ Transaction declined: Insufficient funds available.")
            else:
                acc['account_deposit'] -= amount
                str.success(f"✅ Withdrawal processed! Remaining balance left: ${acc['account_deposit']}")

elif choice == "Transfer Money":
    str.subheader("💸 Inter-Account Transfer Routine")
    sender_num = str.number_input("Your Account Number", min_value=10000, max_value=99999, step=1)
    sender_pin = str.number_input("Your Account PIN", min_value=1000, max_value=9999, step=1)
    
    beneficiary_num = str.number_input("Target Beneficiary Account Number", min_value=10000, max_value=99999, step=1)
    amount = str.number_input("Transfer Value Sum ($)", min_value=1, step=50)
    
    if str.button("Authorize Transfer Wire"):
        sender = find_account(sender_num, sender_pin)
        beneficiary = find_account(beneficiary_num)
        
        if sender == "INVALID_PIN":
            str.error("❌ Your sender account PIN configuration code is invalid!")
        elif sender == "NOT_FOUND":
            str.error("❌ Sender account configuration signature could not be verified.")
        elif beneficiary in ("NOT_FOUND", "INVALID_PIN"):
            str.error("❌ Target beneficiary data node not located within active state structures.")
        elif sender_num == beneficiary_num:
            str.warning("⚠️ Loops not permitted: You cannot wire transfer value sums back into the original sender node.")
        else:
            if amount > sender['account_deposit']:
                str.error("⚠️ Denied: Insufficient transaction routing cover threshold balance details.")
            else:
                sender['account_deposit'] -= amount
                beneficiary['account_deposit'] += amount
                str.success(f"🚀 Value transfer successfully updated to user node {beneficiary['account_title']}!")
                str.info(f"💳 Remaining Sender Balance Asset Profile: ${sender['account_deposit']}")

elif choice == "Delete Account":
    str.subheader("🗑️ Terminate Customer Profile Node")
    acc_num = str.number_input("Target Discard Account Number", min_value=10000, max_value=99999, step=1)
    pin = str.number_input("Verification Security Pin", min_value=1000, max_value=9999, step=1)
    
    str.warning("⚠️ Critical Alert: This data pipeline removal execution action is completely permanent!")
    confirm = str.checkbox("I verify that I wish to remove this data layer profile entirely from core state operations.")
    
    if str.button("Wipe Profile Node Permanently"):
        if not confirm:
            str.error("Please select the tracking validation verification checkbox confirmation matrix toggle first.")
        else:
            result = delete_account(acc_num, pin)
            if "SUCCESSFULLY" in result:
                str.success(result)
            else:
                str.error(f"❌ Operation failure: {result}")

elif choice == "Admin: View All Accounts":
    str.subheader("📊 System Monitoring Registry")
    if len(str.session_state.acc_database) == 0:
        str.info("ℹ️ System inventory database state is currently clear. No active nodes stored.")
    else:
        str.write(f"Total Active Profiles Loaded: {len(str.session_state.acc_database)}")
        str.dataframe(str.session_state.acc_database)



# to run this use this command  python -m streamlit run bank_system.py