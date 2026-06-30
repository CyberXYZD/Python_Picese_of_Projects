print("Welcome to the Asia-X bank. Choose the following options:")
print("1.Check Your Balance")
print("2.Deposit To Account")
print("3.Withdraw From Account")
print("4.Exit")


my_bank_account = 0

def deposit_to_account(my_bank_account):
    check_deposit = True
    while check_deposit:
        deposit_amount = int(input("Enter your deposit amount: "))
        if deposit_amount > 0:
            my_bank_account +=  deposit_amount
            print("Successfully Deposit!")
            return my_bank_account
        else:
            print("Your deposit amount must be greater than 0")
            check_deposit = True




def withdraw_from_account(my_bank_account):
    check_withdraw = True
    while check_withdraw:
        withdraw_amount = int(input("Enter your withdraw amount: "))
        if withdraw_amount < 0:
            print("Your withdraw amount must be greater than 0")

        elif withdraw_amount > my_bank_account:
            print("Your withdraw amount is more than your current balance!!! Check the Balance")

        else:
            my_bank_account -= withdraw_amount
            print("Successfully Withdraw!")
            return my_bank_account





wrong_choose = True
while wrong_choose:
    continue_services = True
    while continue_services:

        try:
            choose = int(input("Enter your choice option:"))
            if choose == 1:
                print("Check Your Balance")
                wrong_choose = False
                print("Your Balance is: ", my_bank_account)

                services = input("Would you like to services choose again? (y/n): ").lower()
                if services == "y":
                    continue_services = True
                else:
                    print("Thank you! Come back soon!")
                    continue_services = False



            elif choose == 2:
                my_bank_account = deposit_to_account(my_bank_account)
                wrong_choose = False


                services = input("Would you like to services choose again? (y/n): ").lower()
                if services == "y":
                    continue_services = True
                else:
                    print("Thank you! Come back soon!")
                    continue_services = False



            elif choose == 3:
                my_bank_account = withdraw_from_account(my_bank_account)
                wrong_choose = False
                services = input("Would you like to services choose again? (y/n): ").lower()
                if services == "y":
                    continue_services = True
                else:
                    print("Thank you! Come back soon!")
                    continue_services = False


            # elif choose != 1 or choose != 2 or choose != 3 or choose != 4:
            elif choose not in [1,2,3,4]:
                print("Wrong option")
                continue_services = True

            else:
                print("Services End. Come back soon!")
                wrong_choose = False
                continue_services = False

        except ValueError:
            print("Please Enter valid option or number")





