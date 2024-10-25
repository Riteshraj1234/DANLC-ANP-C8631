# 8.  input bank login and password and check whether it is valid or not
# if login is successful, then give options to user for the following:-
# 1. Change password
# 2. Check Balance
# 3. Deposit Amount
# 4. Withdraw Amount
userid = 8178777642
pin = 1607
balance = 90500
uid = int(input("Enter userid : "))
if uid == userid:
    upass = int(input("Enter Your PIN : "))
    if upass == pin:
        print("Login Successful!!")
        print("-----------------------------")
        print("1. Change Password")
        print("--------------------------------")
        print("2. Check Balance")
        print("--------------------------------")
        print("3. Deposit Amount")
        print("--------------------------------")
        print("4. Withdraw Amount")
        print("--------------------------------")
        print("5. Exit")
        choice = int(input("Enter Your choice : "))
        if choice == 1:
            npin = int(input("Enter Your Old Pin : "))
            if npin == pin:
                pin = int(input("Enter New Pin : "))
                pin = int(input("Retype New Pin : "))
                print("Password Changed Successfully!! ")
            else:
                print("Enter correct Pin!! ")
        elif choice == 2:
            print("Your Saving Account balance is Rs. ", balance)
        elif choice == 3:
            amt = float(input("Deposit Amount : "))
            balance = balance + amt
            print(f"{amt} Deposit Successfully!!")
            print(f"Total Balance is : {balance}")
        elif choice == 4:
            wamt = float(input("Enter Withdraw amount : "))
            if wamt<=balance:
                balance = balance - wamt
                print("Amount Withdraw Successfully!!")
            else:
                print("Unsufficient Balance")
        elif choice == 5:
            print("GOOD BYE!!")
        else:
            print("Enter Valid Choice!!")
    else:
        print("Enter Correct Pin!!")
else:
    print("User does not Exist !!")