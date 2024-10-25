#Lab4: Write a Pandas program to create a Pivot table and count the manager wise sale and mean value of sale amount.
""""
print("------------------------------------------------------------------------------------------------------------------------")
import pandas as pd
import numpy as np
print("------------------------------------------------------------------------------------------------------------------------")
# Read data from CSV
data = pd.read_csv("C:\\Users\\Ritesh\\Downloads\\salesdata.csv")

# Create DataFrame
df = pd.DataFrame(data)
print(df.head())
print("------------------------------------------------------------------------------------------------------------------------")

# Create a Pivot Table
pivot_table = pd.pivot_table(df,values='Sale_amt', index='Manager', aggfunc=['mean','count'])  
# Display the Pivot Table
print(pivot_table)
print("------------------------------------------------------------------------------------------------------------------------")
"""
import pandas as pd

# Sample data
data = {
    'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A'],
    'Salesperson': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'],
    'SaleAmount': [100, 200, 150, 300, 250, 200]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Pivot Table for total sales by product
product_pivot = pd.pivot_table(df, values='SaleAmount', index='Product', aggfunc='sum')

# Create a Pivot Table for total sales by salesperson
salesperson_pivot = pd.pivot_table(df, values='SaleAmount', index='Salesperson', aggfunc='sum')

# Identify the top-selling product
top_product = product_pivot['SaleAmount'].idxmax()
top_product_amount = product_pivot['SaleAmount'].max()

# Identify the top-selling salesperson
top_salesperson = salesperson_pivot['SaleAmount'].idxmax()
top_salesperson_amount = salesperson_pivot['SaleAmount'].max()

# Display results
print("Total Sales by Product:")
print(product_pivot)
print("\nTotal Sales by Salesperson:")
print(salesperson_pivot)
print(f"\nTop-selling Product: {top_product} with sales of {top_product_amount}")
print(f"Top-selling Salesperson: {top_salesperson} with sales of {top_salesperson_amount}")
