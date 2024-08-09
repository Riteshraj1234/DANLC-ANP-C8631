"""
.Write a Python program to get the key, value and item in a dictionary.
"""
a= {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(a)
for key, value in a.items():
   print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")

