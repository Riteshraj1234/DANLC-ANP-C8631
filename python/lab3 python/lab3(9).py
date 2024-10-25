# 9.  write a program to generate the following payslip for an employee:-
basic = int(input("Enter basic salary: "))
exp = int(input("Enter Experience: "))
name = input("Enter Name: ")

print("--------------------------------------------------------------------------------------------------------\n")
print("                                               Pay Slip                                                 \n")
print("--------------------------------------------------------------------------------------------------------\n")
print(f"Name: {name}")
print(f"Experience: {exp}")
print(f"Basic Salary: {basic}\n")
print("--------------------------------------------------------------------------------------------------------\n")
da=basic*0.05
print(f"DA : {da}")
ta=basic*0.065
print(f"TA : {ta}")
cca=basic*0.08
print(f"CCA : {cca}")
hra=basic*0.10
print(f"HRA : {hra}")
pf=basic*0.125
print(f"PF : {pf}")
if exp > 25:
    bonus = 0.25 * basic
elif exp > 20:
    bonus = 0.20 * basic
elif exp > 15:
    bonus = 0.15 * basic
else:
    bonus = 0.10 * basic
print(f"BONUS : {bonus}")
totalsalary=basic+da+ta+cca+hra+pf+bonus
print(f"TOTAL SALARY : {totalsalary}")
print(f"NET SALARY : {totalsalary-pf}")


print("--------------------------------------------------------------------------------------------------------\n")