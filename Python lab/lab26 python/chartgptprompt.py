"""Scenario:Analyzing Sales Data with a Pivot Table Suppose you work for a retail company, and you have a dataset containing sales data.
The data includes information about sales transactions, products, and salespeople.
You want to create a pivot table to summarize sales by product and salesperson like 
Calculate the total sales for each product,Calculate the total sales for each salesperson,Identify the top-selling product and salesperson.
Create a ChatGPT prompt to generate the code for this scenario. 
Based on the code generated, ask ChatGPT to give the conclusion/inference.
Note. You can provide the data to ChatGPT in the form of a list or dictionary or ask it to use sample data. 
""" 
print("------------------------------------------------------------------------------------------------------------------------")
import pandas as pd
import numpy as np
print("------------------------------------------------------------------------------------------------------------------------")
data = {
    'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A'],
    'Salesperson': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'],
    'SaleAmount': [100, 200, 150, 300, 250, 200]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df.head())

# Create a Pivot Table for total sales by product
product_pivot = pd.pivot_table(df, values='SaleAmount', index='Product', aggfunc=np.sum)

# Create a Pivot Table for total sales by salesperson
salesperson_pivot = pd.pivot_table(df, values='SaleAmount', index='Salesperson', aggfunc=np.sum)
print("------------------------------------------------------------------------------------------------------------------------")
# Identify the top-selling product
top_product = product_pivot['SaleAmount'].idxmax()
top_product_amount = product_pivot['SaleAmount'].max()
print("------------------------------------------------------------------------------------------------------------------------")
# Identify the top-selling salesperson
top_salesperson = salesperson_pivot['SaleAmount'].idxmax()
top_salesperson_amount = salesperson_pivot['SaleAmount'].max()
print("------------------------------------------------------------------------------------------------------------------------")
# Display results
print("Total Sales by Product:")
print(product_pivot)
print("\nTotal Sales by Salesperson:")
print(salesperson_pivot)
print(f"\nTop-selling Product: {top_product} with sales of {top_product_amount}")
print(f"Top-selling Salesperson: {top_salesperson} with sales of {top_salesperson_amount}")
print("------------------------------------------------------------------------------------------------------------------------")