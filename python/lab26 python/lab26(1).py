# Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.

import pandas as pd 
import numpy as np
data = pd.read_csv("C:\\Users\\Ritesh\\Downloads\\salesdata.csv")
# Create DataFrame
df = pd.DataFrame(data)
print(df.head())
print("------------------------------------------------------------------------------------------------------------------------")
# Create a Pivot Table
pivot_table = pd.pivot_table(df, values='Sale_amt', index=['Region', 'Manager', 'SalesMan'], aggfunc=np.sum)
# Display the Pivot Table
print(pivot_table)
print("------------------------------------------------------------------------------------------------------------------------")


