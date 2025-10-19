from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class BankAccount:
    def __init__(self, number, name, balance=0):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
            self.balance += amount
            print(f"✓ deposited ₦ {amount}. New balance: ₦{self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True
    
           
class Bank:
    def __init__(self):
        self.accounts = {}


    def create_account(self, number, name):
        if number in self.accounts:
           return False
        self.accounts[number]=  BankAccount(name, number)
        return True
    def get_account(self, number):
       return self.accounts.get(number) 
             

    def delete_account(self, number):
       if number in self.accounts:
           del self.accounts[number]
           return True
       return False
    
bank = Bank()


@app.route('/')
def index():
    return render_template('index.html', accounts=bank.accounts.values())

@app.route('/create', methods=['POST'])
def create_account():
    number=request.form['account_number']
    name = request.form['account_name']
    if bank.create_account(number, name):
        return redirect(url_for('index'))
    return "Account already exist!", 400


@app.route('/deposit', methods=['POST'])
def deposit():
    number = request.form['account_number']
    amount =float(request.form['amount'])
    acc = bank.get_account(number)
    if acc:
        acc.deposit(amount)
        return redirect(url_for('index'))
    return "Account not found!", 404

@app.route('/withdraw', methods=['POST'])
def withdraw():
    number = request.form['account_number']
    amount = float(request.form['amount'])
    acc = bank.get_account(number)
    if acc:
        if acc.withdraw(amount):
            return redirect(url_for('index'))
        return "Insufficient fund!", 404
    return "Account not found!", 404

@app.route('/delete', methods=['POST'])
def delete():
    number = request.form['account_number']
   
    if bank.delete_account(number):
        return redirect(url_for('index'))
        
    return "Account not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
