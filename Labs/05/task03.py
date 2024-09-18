class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def display_account_info(self):
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: ${self.__account_bal}")
        print(f"Security Code: {self.__security_code}")

my_account = Account(12345678, 5000.75, 9876)
my_account.display_account_info()
