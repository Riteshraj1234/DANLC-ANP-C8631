"""
Write a Python program to get the key, value and item in a dictionary.
"""
A = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}
for key, value in A.items():
    if value is not None:
     print(str(key)+" : "+str(value))
