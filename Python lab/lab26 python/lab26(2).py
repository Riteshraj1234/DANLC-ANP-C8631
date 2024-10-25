# Lab2: Write a Pandas program to create a Pivot table and find the item wise unit sold.
print("------------------------------------------------------------------------------------------------------------------------")
import pandas as pd 
import numpy as np
# Read data from CSV
data = pd.read_csv("C:\\Users\\Ritesh\\Downloads\\salesdata.csv")
# Create DataFrame
df = pd.DataFrame(data)
print(df.head())
print("------------------------------------------------------------------------------------------------------------------------")
pivot_table = pd.pivot_table(df, values='Units', index='Item', aggfunc=np.sum)
#Display the Pivot Table
print(pivot_table)
print("------------------------------------------------------------------------------------------------------------------------")