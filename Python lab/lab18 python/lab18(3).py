import numpy as np

inventory = np.array([10, 0, 5, 0, 20, 0])

out_of_stock = inventory[inventory == 0]

print("Out of Stock Products:", out_of_stock)
