# Lab2: Write a Pandas program to split the following dataframe by school
# code and get mean, min, and max value of age for each school.
# Also generate a horizontal bar chart based on the result and explain the
# conclusion.
# Input:
import pandas as pd
from matplotlib import pyplot as plt

student_data = pd.DataFrame({
        'school_code': ['s001','s002','s003','s001','s002','s004'],
        'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
        'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill','David Parkes'],
        'age': [12, 12, 13, 13, 14, 12],
        'height': [173, 192, 186, 167, 151, 159],
        'weight': [35, 32, 33, 30, 31, 32],
        'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
        )
print(f"Original Dataframe : {student_data}")
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

print("Mean , min and Max value of age for each value of the school : ")
print(age_stats)

age_stats.plot(kind='barh')

plt.xlabel('Age')
plt.ylabel('School_Code')
plt.title('Mean, Min, and Max Age per School Code')
plt.show()