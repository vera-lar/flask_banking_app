from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class BankAccount:
    def __init__(self, account_number, account_name, balance=0.0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
            if amount > 0:
               self.balance += amount
               return True
             # print(f"✓ deposited ₦ {amount}. New balance: ₦{self.balance}")
            return False
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
       # self.balance += amount
        return False
    def get_balance(self):
        return self.balance
    
    def display_info(self):
        return f"{self.account_name} -{self.account_number}:  ₦{self.balance:. 2f}"
           
class Bank:
    def __init__(self):
        self.accounts = {}


    def create_account(self, account_number, account_name):
        if account_number not in self.accounts:   
            self.accounts[account_number]=  BankAccount(account_name, account_number)
            return True
        return False
    
    def delete_account(self, account_number):
       if account_number in self.accounts:
           del self.accounts[account_number]
           return True
       return False
    
    def get_account(self, account_number):
       return self.accounts.get(account_number) 
             
    def all_accounts(self):
        return self.accounts#.values()
   
   #routes
bank = Bank()


@app.route('/')
def index():
    return render_template('index.html', accounts=bank.all_accounts().values())

@app.route('/create', methods=['POST'])
def create_account():
    use_number=request.form['account_number']
    use_name =request.form['account_name']
    #balance = request.form['balance']
    acc = bank.create_account(use_number,use_name)
    return redirect(url_for('index'))
    #return "Account already exist!", 400


@app.route('/deposit', methods=['POST'])
def deposit():
    account_number = request.form['account_number']
    amount =float(request.form['amount'])
    acc = bank.get_account(account_number)
    if acc:
        acc.deposit(amount)
    return redirect(url_for('index'))
   # return "Account not found!", 404

@app.route('/withdraw', methods=['POST'])
def withdraw():
    account_number = request.form['account_number']
    amount = float(request.form['amount'])
    acc = bank.get_account(account_number)
    if acc:
        acc.withdraw(amount)
    return redirect(url_for('index'))
       # return "Insufficient fund!", 404
   # return "Account not found!", 404

@app.route('/delete', methods=['POST'])
def delete():
    account_number = request.form['account_number']
   
    bank.delete_account(account_number)
    return redirect(url_for('index'))
        
   # return "Account not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
