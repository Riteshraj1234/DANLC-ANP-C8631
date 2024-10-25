# 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.
import numpy as np

a = np.full(10,0,dtype=float)
b = np.full(10,1,dtype=float)
c = np.full(10,5,dtype=float)
print("An Array of 10 Zero : ",a)
print("An Array of 10 One : ",b)
print("An Array of 10 Five : ",c)