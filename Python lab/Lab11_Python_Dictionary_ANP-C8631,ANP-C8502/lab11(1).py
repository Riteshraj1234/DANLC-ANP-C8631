"""
Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

"""
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
print(test_dict)
#mean value
mean_value = sum(test_dict.values()) / len(test_dict)
# Print the mean
print("The mean of the values in the dictionary is:", mean_value)
