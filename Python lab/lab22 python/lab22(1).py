"""
Suppose you are a teacher, and you want to analyze the exam scores of your
students in a particular subject. You have recorded the scores of your students for a
recent exam, and you want to represent this data using a Pandas Series.
"""

import pandas as pd


students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]
# Create a Pandas Series with months as the index
Name = pd.Series(exam_scores , index=students ,name= 'exam_scores')
# Display the Series
print(Name)





