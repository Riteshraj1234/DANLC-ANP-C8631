"""
Suppose you want to track and analyze your household expenses for a month.
You have recorded the expenses for various categories, such as groceries, utilities, rent,
transportation, and entertainment. You can represent this expense data using a Pandas
Series.
"""


import pandas as pd

# Expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
# Monthly expense data (example data in USD)
expenses = [500, 200, 1200, 300, 150]
# Create a Pandas Series with months as the index
sales_series = pd.Series(expenses, index=categories, name='Monthly Sales (USD)')
# Display the Series
print(sales_series)