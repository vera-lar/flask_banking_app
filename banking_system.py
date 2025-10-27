class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✓ deposited ₦ {amount}. New balance: ₦{self.balance}")
        else:
            print("✕ deposit amount must be positive. ")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insuficient balance")
        elif amount <= 0:
            print(f"withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print("withdraw ₦ {amount}. New balamce: ₦ {self.balance}")

    def check_balance(self):
        print(f" {self.balance}'s Current balance: ₦{self.balance}")

    def display_account_info(self):
        print("\n---Account Info")
        print(f" Account Number : {self.account_number}")
        print(f"Accountname : {self.account_name}")
        print(f"balance :₦ {self.balance}")
        print("--------------")
            
            
           
class Bank:
    def __init__(self):
        self.accounts = {}


    def create_account(self, account_number, account_name, initial_deposit=0):
        if account_number in self.accounts:
            print("Account number already exists")
        else:
            account = BankAccount(account_name, account_number, initial_deposit)
            self.accounts[account_number] = account
            print("Account created succesfully for {account_name}! ")


    def delete_account(self, account_number):
       if account_number in self.accounts:
           del self.accounts[account_number]
           print(f"🗑️ Accout {account_number} deleted successfully.")
       else:
           print(f"Account not found.")


    def display_all_accounts(self):
        if not self.accounts:
            print(f"No accpunt found ")

        else:
            print("\n === All Bank Accounts === ")
            for acc in self.accounts.values():
                acc.display_account_info()

                # ----interactive menu
def main():
    bank = Bank()

    while True:
            print("\n==== simple banking system ====")
            print(" 1. create Account")
            print(" 2. deposit money")
            print(" 3. withdraw money")
            print(" 4. cheack balance")
            print(" 5. delete account")
            print(" 6. display all accounts")
            print(" 7. Exit")
            
            choice = input("Select an option (1-7): ")
            if choice == "1":
                acc_no = float(input("Enter phone_number: "))
                name = input("Enter account name: ")
                bank.create(acc_no,name)
                print(f"{name} your account number is {acc_no}")
                  #deposit = float(input("Enter initail deposit: "))
                
            elif choice == "2":
                acc_no = input("Enter account number: ")
                if acc_no in bank.accounts:
                    amount = float(input("Enter deposit amount:"))
                    bank.accounts[acc_no].deposit(amount)
                else:
                    print("Account not found")
           
            elif choice == "3":
                acc_no = input("Enter account number: ")
                if acc_no in bank.accounts:
                    amount = float(input("Enter withdrawal amount:"))
                    bank.accounts[acc_no].withdraw(amount)
                else:
                    print("Account not found")
           
            elif choice == "4":
                acc_no = input("Enter account number: ")
                if acc_no in bank.accounts:
                    bank.accounts[acc_no].check_balance()
                else:
                    print("Account not found")
            
            elif choice == "5":
                acc_no = input("Enter account number to be delete: ")
                
                bank.delete_account[acc_no]
          
            elif choice == "6":
                bank.display_all_accounts()
               
            elif choice == "7":
                print("Thank you for using our banking system. have a nice day!")
                break
            else:
                print("Invalid option. please select between 1 to 7. ")


if __name__ == "__main__":
        main()