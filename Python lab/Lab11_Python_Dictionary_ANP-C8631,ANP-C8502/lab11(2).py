"""
Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
combined_dict = {}
for i in (dic1, dic2, dic3):
    combined_dict.update(i)
print("The concatenated dictionary is:", combined_dict)