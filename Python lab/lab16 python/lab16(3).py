# 3. Suppose you have a dataset containing customer data, and you want to split this data
# into two groups: one group for customers who made a purchase in the last 30 days and
# another group for customers who haven't made a purchase in the last 30 days.
# Input:
import numpy as np

customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
indices = np.where(last_purchase_days_ago <= 30 )[0]
id = customer_ids[indices]
print("Active customers IDs: ")
print(id)
indices2 = np.where(last_purchase_days_ago > 30)[0]
id2 = customer_ids[indices2]
print("Unactive Customers IDs: ")
print(id2)