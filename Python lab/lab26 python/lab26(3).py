# Lab3: Write a Pandas program to create a Pivot table and find the region wise, item wise & unitsold.

import pandas as pd
import numpy as np
print("------------------------------------------------------------------------------------------------------------------------")
# Read data from CSV
data = pd.read_csv("C:\\Users\\Ritesh\\Downloads\\salesdata.csv")
# Create DataFrame
df = pd.DataFrame(data)
print(df.head())
print("------------------------------------------------------------------------------------------------------------------------")
pivot_table = pd.pivot_table(df, values='Units', index=['Region', 'Item'], aggfunc=np.sum,) 
# print the Pivot Table
print(pivot_table)
print("------------------------------------------------------------------------------------------------------------------------")