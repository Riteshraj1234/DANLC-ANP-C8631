#3. Wap to check login and password.

userid = "riteshk57314@gmail.com"
pass1 = "Ritesh@123"

uid = input("Enter Email-id : ")

if uid == userid:
    upass = input("Enter your password : ")
    if upass == pass1:
        print("Login Successful !!")
    else:
        print("Incorrect Password !!")
else:
    print("User does not exists!!")