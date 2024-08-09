salary=float(input("enter your salary:"))
Da= salary*0.02
print(Da)
Ta=0.03*salary
print(Da)
Hra=0.10*salary
print(Da)
PF=0.15*salary
print(PF)
Total_salary=(salary +Da + Ta + Hra + PF)
print(Total_salary)
net_salary =int(Total_salary-PF)
print(net_salary)
bonus=(net_salary>>2)
print(f"your bonus:{bonus}")
