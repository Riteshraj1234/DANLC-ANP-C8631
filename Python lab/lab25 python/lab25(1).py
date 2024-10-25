"""
Lab1: Write a Pandas program to split the following data frame into groups based
on Class and count the number of students in that particular class.Also generate
a bar chart based on the result and explain the conclusion.
Input:
student_data = pd.DataFrame({
'school_code': ['s001','s002','s003','s001','s002','s004'],
'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill',
'David Parkes'],
'age': [12, 12, 13, 13, 14, 12],
'height': [173, 192, 186, 167, 151, 159],
'weight': [35, 32, 33, 30, 31, 32],
'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']})
"""

import pandas as pd


# Create the DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})
class_counts = student_data.groupby('class')['name'].count()

print("Number of students in each class:")
print(class_counts)
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 6))
plt.bar(class_counts.index, class_counts.values, color='red', edgecolor='black')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.title('Student Counts by Class')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
