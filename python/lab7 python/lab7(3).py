# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
# Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
# Output:
# UpperCase : 5
# LowerCase : 18
# NumberCase : 5
# SpecialCase : 11
str = input("Enter a string : ")
uperc = 0
lowerc = 0
char = 0
numb = 0

for i in str:
    if ord(i) > 31 and ord(i) < 48:
        char += 1
    elif ord(i) > 47 and ord(i) < 58:
        numb += 1
    elif 65 <= ord(i) <= 90:
        uperc += 1
    elif 97 <= ord(i) <= 122:
        lowerc += 1
print(f"the total No. of UpperCase is : {uperc}")
print(f"the total No. of LowerCase is : {lowerc}")
print(f"the total No. of Numbers is : {numb}")
print(f"the total No. of SpecialCase is : {char}")
