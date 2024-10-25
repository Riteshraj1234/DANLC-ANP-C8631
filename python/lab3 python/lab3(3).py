#3. Wap to check login and password.

userid = "admin@gmail.com"
pass1 = "admin@123"

uid = input("Enter Email-id : ")

if uid == userid:
    upass = input("Enter your password : ")
    if upass == pass1:
        print("Login Successful !!")
    else:
        print("Incorrect Password !!")
else:
    print("User does not exists!!")