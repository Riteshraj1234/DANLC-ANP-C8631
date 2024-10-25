#Wap to check whether a character is alphabet, number or special character.

char=ord(input("Enter any Character : "))
if 65<= char <= 90 or 97<= char <= 122 :
    print("Given character is Alphabet")
if 33<= char <= 47 or 58<= char <= 64 or 91<= char <= 96 or 123<= char <= 127 :
    print("Give value is special character")
if 48<= char <= 57:
    print("given character is Number")
