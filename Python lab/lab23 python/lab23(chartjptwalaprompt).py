"""
Scenario: Analyzing Sales Data
Suppose you work for a retail company, and you have a dummy dataset containing
sales data for the past year. The data includes information such as customer names,
product names, sales quantities, prices, and dates. You want to perform various data
analysis tasks like Total revenue for the year,Average revenue per sale,Best-selling
product,Date with the highest total revenue also wants to generate product and total
sales wise barchart using Pandas DataFrames.
Further, you need to get some inference out of the chart.
Create a ChatGPT prompt to generate the code for this scenario. Based on the code
generated, ask ChatGPT to give the conclusion/inference.
Note. You can provide the data to ChatGPT in the form of a list or dictionary or ask it to use sample data.
Sample sales data
data = {
    'Customer': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice'],
    'Product': ['Laptop', 'Laptop', 'Tablet', 'Tablet', 'Laptop', 'Tablet', 'Smartphone'],
    'Quantity': [1, 2, 1, 2, 1, 3, 1],
    'Price': [1000, 1000, 500, 500, 1000, 500, 800],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07']
}
"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    'Customer': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice'],
    'Product': ['Laptop', 'Laptop', 'Tablet', 'Tablet', 'Laptop', 'Tablet', 'Smartphone'],
    'Quantity': [1, 2, 1, 2, 1, 3, 1],
    'Price': [1000, 1000, 500, 500, 1000, 500, 800],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07']
}

# Creating a DataFrame
df = pd.DataFrame(data)

print("Original Data")
print("--------------------------------------------------------------------")
print(df)
print("--------------------------------------------------------------------")
print("question 2: \n")
# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Total Revenue (Price * Quantity)
df['Revenue'] = df['Price'] * df['Quantity']

# Output the DataFrame with the new 'Revenue' column
print("Data with Revenue Calculated")
print("--------------------------------------------------------------------")
print(df)
print("--------------------------------------------------------------------")

# 1. Calculate the total revenue for the year
total_revenue = df['Revenue'].sum()
print(f"Total revenue for the year: ${total_revenue}")
print("--------------------------------------------------------------------")
print("Average Revenue per Sale :\n")
# 2. Average revenue per sale
average_revenue = df['Revenue'].mean()
print(f"Average revenue per sale: ${average_revenue:.2f}")
print("--------------------------------------------------------------------")
print(" Best-Selling Product :")
# 3. Best-selling product
best_selling_product = df.groupby('Product')['Quantity'].sum().idxmax()
print(f"Best-selling product: {best_selling_product}")
#print("--------------------------------------------------------------------")
print("Date with the Highest Total Revenue :\n")
print("--------------------------------------------------------------------")
# 4. Date with the highest total revenue
date_highest_revenue = df.groupby('Date')['Revenue'].sum().idxmax()
print(f"Date with the highest total revenue: {date_highest_revenue.date()}")
print("--------------------------------------------------------------------")
print("Product vs. Total Sales : \n")
print("create a bar chart:\n")
print("--------------------------------------------------------------------")
# 5. Generate bar charts
Barchart:Products vs. TotalSales # type: ignore
product_sales = df.groupby('Product')['Revenue'].sum()
product_sales.plot(kind='bar', title='Product vs. Total Sales', xlabel='Product', ylabel='Total Sales', color='skyblue')
plt.show()
print("--------------------------------------------------------------------")
print("Date vs. Total Sales Chart: \n")
print("--------------------------------------------------------------------")
# Bar chart: Dates vs. Total Sales
date_sales = df.groupby('Date')['Revenue'].sum()
date_sales.plot(kind='bar', title='Date vs. Total Sales', xlabel='Date', ylabel='Total Sales', color='orange')
plt.show()
print(f"Date with the highest total revenue: {date_highest_revenue.date()}")
print("--------------------------------------------------------------------")

