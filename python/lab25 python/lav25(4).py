# Lab4: Write a Pandas program to split the following data frame into groups
# and calculate monthly purchase amount.Also generate a bar chart based on
# the result and explain the conclusion.
# Input:
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({
        'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
        'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
        'ord_date':['05-10-2012','09-10-2012','05-10-2012','08-17-2012','10-09-2012','07-27-2012','10-09-2012','10-10-2012','10-10-2012','06-17-2012','07-08-2012','04-25-2012'],
        'customer_id':[3001,3001,3005,3001,3005,3001,3005,3001,3005,3001,3005,3005],
        'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})

grouped = df.groupby('customer_id')['purch_amt'].agg(['mean', 'min', 'max'])
print(grouped)
grouped.plot(kind='bar')

plt.xlabel('Customer ID')
plt.ylabel('Purchase Amount')
plt.title('Mean, Min, and Max Purchase Amount by Customer ID')
plt.show()