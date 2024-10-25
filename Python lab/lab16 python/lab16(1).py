# 1. Suppose you have a dataset containing daily temperature readings for a city, and you
# want to identify days with extreme temperature conditions. Find days where the
# temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees
# Celsius (cold day).
# Input:
import numpy as np

days = np.arange(1,16)
temp = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])
d = np.where(temp>35)[0]
d1 = days[d]
t = temp[d]
print("Hot days : ")
print("Days:  Temperature")
v = np.vstack((d1,t)).T
print(v)
d2 = np.where(temp < 5)[0]
d3 = days[d2]
t2 = temp[d2]
v2 = np.vstack((d3,t2)).T
print()
print("Cold Days : ")
print("Days:  Temperature")
print(v2)

