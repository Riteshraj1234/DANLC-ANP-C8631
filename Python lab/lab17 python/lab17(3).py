import numpy as np

arr = np.array([20, 2, 7, 1, 34], dtype=np.float64)

print("arr:", arr.tolist())
std_dev = np.std(arr, dtype=np.float64)

print("std of arr:", std_dev)
print(" more precision with float64:\n""std of arr:", std_dev)
print("more accuracy with float64:\n","std of arr:", std_dev)
