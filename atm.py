import tkinter as tk
from tkinter import simpledialog

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.2f}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: ${amount:.2f}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0.0):
        if account_number in self.accounts:
            return "Account number already exists"
        else:
            account = Account(account_number, account_holder, initial_balance)
            self.accounts[account_number] = account
            return "Account created successfully"

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title, message):
        self.message = message
        super().__init__(parent, title)

    def body(self, master):
        self.configure(bg="#e0e0e0")
        tk.Label(master, text=self.message, bg="#e0e0e0", font=("Arial", 12)).pack(padx=20, pady=20)

    def buttonbox(self):
        box = tk.Frame(self, bg="#e0e0e0")
        tk.Button(box, text="OK", width=10, command=self.ok, bg="#4caf50", fg="white").pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        box.pack()

class ATMApp:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("ATM Banking System")

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#f5f5f5")
        self.frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame, text="ATM Banking System", font=("Arial", 16), bg="#f5f5f5")
        self.label.grid(row=0, columnspan=2, pady=10)

        self.account_label = tk.Label(self.frame, text="Account Number:", bg="#f5f5f5")
        self.account_label.grid(row=1, column=0, pady=5, sticky='e')
        self.account_entry = tk.Entry(self.frame)
        self.account_entry.grid(row=1, column=1, pady=5)

        self.holder_label = tk.Label(self.frame, text="Account Holder:", bg="#f5f5f5")
        self.holder_label.grid(row=2, column=0, pady=5, sticky='e')
        self.holder_entry = tk.Entry(self.frame)
        self.holder_entry.grid(row=2, column=1, pady=5)

        self.balance_label = tk.Label(self.frame, text="Initial Balance:", bg="#f5f5f5")
        self.balance_label.grid(row=3, column=0, pady=5, sticky='e')
        self.balance_entry = tk.Entry(self.frame)
        self.balance_entry.grid(row=3, column=1, pady=5)

        self.create_button = tk.Button(self.frame, text="Create Account", command=self.create_account, bg="blue", fg="white")
        self.create_button.grid(row=4, columnspan=2, pady=10)

        self.action_label = tk.Label(self.frame, text="Select Action:", bg="pink")
        self.action_label.grid(row=5, columnspan=2, pady=5)

        self.deposit_button = tk.Button(self.frame, text="Deposit", command=self.deposit, bg="#4caf50", fg="white")
        self.deposit_button.grid(row=6, column=0, pady=5)

        self.withdraw_button = tk.Button(self.frame, text="Withdraw", command=self.withdraw, bg="#ff5722", fg="white")
        self.withdraw_button.grid(row=6, column=1, pady=5)

        self.balance_button = tk.Button(self.frame, text="Check Balance", command=self.check_balance, bg="#9c27b0", fg="white")
        self.balance_button.grid(row=7, columnspan=2, pady=5)

    def create_account(self):
        account_number = self.account_entry.get()
        account_holder = self.holder_entry.get()
        try:
            initial_balance = float(self.balance_entry.get())
        except ValueError:
            CustomDialog(self.root, "Error", "Invalid initial balance")
            return

        message = self.bank.create_account(account_number, account_holder, initial_balance)
        CustomDialog(self.root, "Info", message)

    def deposit(self):
        account_number = self.account_entry.get()
        account = self.bank.get_account(account_number)
        if account:
            try:
                amount = float(self.balance_entry.get())
            except ValueError:
                CustomDialog(self.root, "Error", "Invalid deposit amount")
                return
            message = account.deposit(amount)
            CustomDialog(self.root, "Info", message)
        else:
            CustomDialog(self.root, "Error", "Account not found")

    def withdraw(self):
        account_number = self.account_entry.get()
        account = self.bank.get_account(account_number)
        if account:
            try:
                amount = float(self.balance_entry.get())
            except ValueError:
                CustomDialog(self.root, "Error", "Invalid withdrawal amount")
                return
            message = account.withdraw(amount)
            CustomDialog(self.root, "Info", message)
        else:
            CustomDialog(self.root, "Error", "Account not found")

    def check_balance(self):
        account_number = self.account_entry.get()
        account = self.bank.get_account(account_number)
        if account:
            balance = account.get_balance()
            CustomDialog(self.root, "Balance", f"Balance: ${balance:.2f}")
        else:
            CustomDialog(self.root, "Error", "Account not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
