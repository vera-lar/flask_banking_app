from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class BankAccount:
    def __init__(self, number, name, balance=0.0):
        self.number = number
        self.name = name
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
        return f"{self.name} -{self.number}:  ₦{self.balance:. 2f}"
           
class Bank:
    def __init__(self):
        self.accounts = {}


    def create_account(self, number, name):
        if number not in self.accounts:   
            self.accounts[number]=  BankAccount(name, number)
            return True
        return False
    
    def delete_account(self, number):
       if number in self.accounts:
           del self.accounts[number]
           return True
       return False
    
    def get_account(self, number):
       return self.accounts.get(number) 
             
    def all_accounts(self):
        return self.accounts.values()
   
   #routes
bank = Bank()


@app.route('/')
def index():
    return render_template('index.html', accounts=bank.all_accounts.values())

@app.route('/create', methods=['POST'])
def create_account():
    use_number=request.form['account_number']
    use_name = request.form['account_name']
    bank.create_account(use_number, use_name)
    return redirect(url_for('index'))
    #return "Account already exist!", 400


@app.route('/deposit', methods=['POST'])
def deposit():
    number = request.form['account_number']
    amount =float(request.form['amount'])
    acc = bank.get_account(number)
    if acc:
        acc.deposit(amount)
    return redirect(url_for('index'))
   # return "Account not found!", 404

@app.route('/withdraw', methods=['POST'])
def withdraw():
    number = request.form['account_number']
    amount = float(request.form['amount'])
    acc = bank.get_account(number)
    if acc:
        acc.withdraw(amount)
    return redirect(url_for('index'))
       # return "Insufficient fund!", 404
   # return "Account not found!", 404

@app.route('/delete', methods=['POST'])
def delete():
    number = request.form['account_number']
   
    bank.delete_account(number)
    return redirect(url_for('index'))
        
   # return "Account not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
