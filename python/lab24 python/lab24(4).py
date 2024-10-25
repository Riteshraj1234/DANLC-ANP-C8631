# Write a Pandas program to drop those rows from a given DataFrame in
# which specific columns have missing values.
# Input:
# df = pd.DataFrame({
# 'ord_no':[np.nan,np.nan,70002,np.nan,np.nan,70005,np.nan,70010,70003,70012,np.n
# an,np.nan],
# 'purch_amt':[np.nan,270.65,65.26,np.nan,948.5,2400.6,5760,1983.43,2480.4,250.45,
# 75.29,np.nan],
# 'ord_date':
# [np.nan,'2012-09-10',np.nan,np.nan,'2012-09-10','2012-07-27','2012-09-10','2012-10-
# 10','2012-10-10','2012-06-27','2012-08-17',np.nan],
# 'customer_id':[np.nan,3001,3001,np.nan,3002,3001,3001,3004,3003,3002,3001,np.na
# n]})

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ord_no': [np.nan, np.nan, 70002, np.nan, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, np.nan],
    'purch_amt': [np.nan, 270.65, 65.26, np.nan, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, np.nan],
    'ord_date': [np.nan, '2012-09-10', np.nan, np.nan, '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', np.nan],
    'customer_id': [np.nan, 3001, 3001, np.nan, 3002, 3001, 3001, 3004, 3003, 3002, 3001, np.nan]
})
print("==========================Ritesh Raj==================÷÷÷÷==========")

columns_to_check = ['ord_no', 'purch_amt', 'ord_date']

df_cleaned = df.dropna(subset=columns_to_check)

print("DataFrame after dropping rows where specified columns have missing values:")
print(df_cleaned)
print("==========================Ritesh Raj===================================")