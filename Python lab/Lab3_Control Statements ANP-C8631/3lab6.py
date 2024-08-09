"""6.    Input units of electricity from user and print the bill according to the following criteria
a.    Less than 200 : no bill
b.    Next 200-300  -   1.2/perunit       100*1
c.     Next 300-400  -1.5/perunit           100*2
d.    Next 400-500  - 2.5/perunit          100*3
e.    Above 500 -   8/per unit"""
elec=float(input("Enter Unit of electricity used : "))
if elec>500 :
    print("Bill : ",elec*8 )
if 400<=elec<=500 :
    print("Bill : ",elec*2.5 )
if 300<=elec<400 :
    print("Bill : ",elec*1.5 )
if 200<=elec<300:
    print("Bill : ",elec*1.2 )
if 200>elec:
    print("You have No Bill !!!" )

