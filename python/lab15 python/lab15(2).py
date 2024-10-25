# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
import numpy as np

a = np.arange(2,11)
b = a.reshape(3,3)
print(b)
