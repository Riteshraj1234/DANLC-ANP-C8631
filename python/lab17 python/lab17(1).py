import numpy as np

list_of_arrays = [np.array([3, 2, 8, 9]), np.array([4, 12, 34, 25, 78]), np.array([23, 12, 67])]

means = [np.mean(array) for array in list_of_arrays]

print("Mean for each array:\n", means)
