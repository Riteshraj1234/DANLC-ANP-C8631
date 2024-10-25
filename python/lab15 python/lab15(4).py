# 4. Write a NumPy program to convert a list and tuple into arrays.
# Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# Input: my_tuple = ([8, 4, 6], [1, 2, 3])
import numpy as np

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])
a = np.array(my_list)
b = np.array(my_tuple)
print(a)
print(b)