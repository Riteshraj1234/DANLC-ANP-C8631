"""
 Create a bar chart to represent monthly expenses in different spending
categories and give your conclusion
"""

import matplotlib.pyplot as plt
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
# Monthly expenses in dollars (replace with your own data)
expenses = [1200, 400, 200, 150, 250]
plt.bar(categories,expenses,color = "purple")
plt.title("Monthly expense Breakout ")
plt.xlabel("Expense categories")
plt.ylabel("Monthly Expenses(USD)")

plt.show()
plt.show()
