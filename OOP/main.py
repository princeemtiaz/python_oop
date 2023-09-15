from bank import Bank
from users import Acc_holder, Admin


def main():
    # Registering a Bank from Bangladesh Bank named phitron
    phitron = Bank("Phitron")

    # Creating user accounts
    rifat_vai = Acc_holder(
        "Emtiaz", "emtiaz2060@gmail.com", "Natore", 500
    )
    asif_vai = Acc_holder("Asif Iqbal", "as.iqbal@gmail.com", "Chittagong", 500)
    emdad_vai = Acc_holder("Emdadul Haque Tareq", "em.tareq@gmail.com", "Dhaka", 500)

    # Adding newly created accounts to the bank server
    phitron.create_new_account(rifat_vai)
    phitron.create_new_account(asif_vai)
    phitron.create_new_account(emdad_vai)

    # User operations
    rifat_vai.deposit(5000)
    rifat_vai.check_balance()
    rifat_vai.transfer_balance(500, asif_vai)
    rifat_vai.transfer_balance(1500, asif_vai)
    rifat_vai.check_balance()
    asif_vai.check_balance()

    asif_vai.take_loan(1500, phitron)
    asif_vai.check_balance()
    rifat_vai.see_transaction_history()
    asif_vai.see_transaction_history()

    asif_vai.withdraw(1000)

    # Adding admin
    password = "password"
    admin = Admin("admin", "admin@gmail.com", password)
    phitron.admins[password] = admin

    phitron.toggle_loan_on_off(password)

    asif_vai.take_loan(1500, phitron)

    # Admin operations
    print("\nAdmin access only\n")
    phitron.toggle_loan_on_off(password)
    print("\n==============Current Bank State=================")
    print("Balance: ", end=" ")
    print(admin.total_bank_balance(phitron))
    print("Loan Given: ", end=" ")
    print(admin.total_loan_given(phitron))
    print("Net Balance: ", end=" ")
    print(phitron.net_balance())
    print("==============Ends Here=================\n")

    print("Admin access only\n")
    print("==============Account Details=================")
    print(phitron)
    print("==============Ends Here=================")


if __name__ == "__main__":
    main()
