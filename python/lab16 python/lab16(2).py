# 2. Suppose you have a dataset containing monthly sales data for a company, and you
# want to split this data into quarterly reports for analysis and reporting purposes.
# Input:
import numpy as np

monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
a = np.split(monthly_sales,4)
print(a)
count = 1
for i in a:
    print(f"Quater {count} sales:")
    print(i)
    print()
    count += 1