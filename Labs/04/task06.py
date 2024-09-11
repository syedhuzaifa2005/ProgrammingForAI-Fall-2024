class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0.0, date_of_opening=None):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        """Check the account balance."""
        print(f"Account Balance: ${self.balance:.2f}")
    
    def account_info(self):
        """Print account information."""
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ${self.balance:.2f}")

if __name__ == "__main__":
    account = BankAccount(account_number="123456789", customer_name="Huzaifa", initial_balance=1000.0)

    account.account_info()

    account.deposit(500.0)

    account.withdraw(200.0)

    account.check_balance()
