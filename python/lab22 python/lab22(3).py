"""
Suppose you want to track and analyze the monthly energy consumption in your
home. You have recorded the monthly energy usage for electricity and gas over a year,
and you want to represent this data using Pandas Series.
"""


import pandas as pd

# Months in a year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
# Monthly energy consumption data (example data in kilowatt-hours for electricity and therms for gas)
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]
Name = pd.Series(electricity_usage,  index=months   ,name= 'electricity_usage')
print(Name)
Name1 = pd.Series(gas_usage,  index=months   ,name= 'gas_usage')
print(Name1)
