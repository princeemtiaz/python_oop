from datetime import datetime


class Bank:
    __acc_number_start = 1000
    __loan_application_open = True

    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.admins = {}
        self.total_balance = 0
        self.total_loan = 0

    def create_new_account(self, account):
        account_number = self.generate_acc_no()
        self.accounts[account_number] = account

    def generate_acc_no(self):
        self.__acc_number_start += 1
        return self.__acc_number_start

    def _update_total_balance(self):
        self.total_balance = sum(acc.balance for acc in self.accounts.values())

    def _update_total_loan(self):
        self.total_loan = sum(acc.loaned for acc in self.accounts.values())

    def total_bank_balance(self):
        self._update_total_balance()
        return self.total_balance

    def total_loan_given(self):
        self._update_total_loan()
        return self.total_loan

    def net_balance(self):
        return self.total_balance - self.total_loan

    def toggle_loan_on_off(self, password):
        admin = self.admins.get(password)
        if admin:
            self.__loan_application_open = not self.__loan_application_open
            print(
                "Loan feature has been enabled."
                if self.__loan_application_open
                else "Loan feature has been disabled."
            )
        else:
            print("Invalid admin password.")

    def get_loan_application_status(self):
        return self.__loan_application_open

    def __repr__(self):
        acc_details = f"Bank: {self.name}\n"
        acc_details += "---------------------------\n"
        for acc_no, acc in self.accounts.items():
            acc_details += f"Account Number: {acc_no}\n"
            acc_details += f"Account Details:\n{acc}\n"
        return acc_details
