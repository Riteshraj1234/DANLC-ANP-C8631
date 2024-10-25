# Hi! I have two column Date and sales with some dummy data. Can you please generate
# a line chart based on these two columns ?
# After generating the code using chatgpt, run the code, display the output and explain
# the conclusion.

import matplotlib.pyplot as plt
from datetime import datetime

# Sample data
dates = ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01']
sales = [100, 150, 200, 250, 300]

# Convert dates from string to datetime objects
dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(dates, sales, marker='o', linestyle='-', color='b')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()
