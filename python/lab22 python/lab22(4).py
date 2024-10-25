"""
Suppose you are managing a website and want to analyze the monthly revenue
generated from advertising. You have recorded the monthly revenue for the past year,
and you want to represent this data using a Pandas Series.
"""

import pandas as pd

# Months in a year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
# Monthly advertising revenue data (example data in USD)
revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]

Name = pd.Series(revenue,  index=months  ,name= 'advertising revenue(USD)')
print(Name)