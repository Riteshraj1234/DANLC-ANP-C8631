# Lab3: Write a Pandas program to split a dataset, group by one column and
# get mean, min, and max values by group. Using the following dataset find
# the mean, min, and max values of purchase amount (purch_amt) group by
# customer id (customer_id).Also generate a line chart based on the result and
# explain the conclusion.
# Input:
import pandas as pd
from matplotlib import pyplot as plt

orders_data = pd.DataFrame({
        'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
        'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
        'ord_date':['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
        'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
        'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})

print(f"Original order Datasets : {orders_data}")
orders_data['ord_date'] = pd.to_datetime(orders_data['ord_date'])

monthly_purch_amt = orders_data.set_index('ord_date').resample('M')['purch_amt'].sum()
print(monthly_purch_amt)

monthly_purch_amt.plot(kind='line', marker='o')
plt.xlabel('Order Date')
plt.ylabel('Purchase Amount')
plt.title('Month-wise Purchase Amount')
plt.show()