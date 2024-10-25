# Write a Pandas program to drop the rows where at least one element is
# missing in a given DataFrame.
# Input:
# df = pd.DataFrame({
# 'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.na
# n,70013],
# 'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,
# 75.29,3045.6],
# 'ord_date':
# ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10'
# ,'2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
# 'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
# 'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.n
# an]})

import pandas as pd
import numpy as np

# Create the DataFrame with the provided data
df = pd.DataFrame({
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]
})
print("==========================Ritesh Raj======================")
df_cleaned = df.dropna()

print("DataFrame after dropping rows with at least one missing value:")
print(df_cleaned)
print("==========================Ritesh Raj======================")