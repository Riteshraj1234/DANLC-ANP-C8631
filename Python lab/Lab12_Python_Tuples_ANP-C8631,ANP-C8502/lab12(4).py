"""
write a Python program and iterate the given tuple.
"""
employee1 =("Ritesh Raj",101,"human resource ",60000)
employee2 =("Ranjeet Bhaskar",101,"human resource ",60000)
employee3 =("Nitish matha",101,"human resource ",60000)
employ = (employee1,employee2,employee3)
print("Employee Record :  \n")
for i in employ:
    name, employee_id, department, salary = i
    print(f"Name : {name}")
    print(f"Employee ID : {employee_id}")
    print(f"Department : {department}")
    print(f"Salary : ₹{salary}\n")