
balance = 1000
transactions = []

def display_balance():
    print("\n===== Account Balance =====")
    print("Available Balance: ₹", balance)

def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: ₹ "))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")

def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: ₹ "))

    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        transactions.append(f"Withdrawn ₹{amount}")
        print("Please collect your cash.")

def show_statement():
    print("\n===== Transaction Statement =====")

    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)

def atm():
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")
        print("================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_balance()

        elif choice == 2:
            deposit_money()

        elif choice == 3:
            withdraw_money()

        elif choice == 4:
            show_statement()

        elif choice == 5:
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

atm()