"""
Visualize the daily temperature changes over time in a city and give your
conclusion
"""

import matplotlib.pyplot as plt

days = list(range(1, 32))
# Daily temperature data (replace with your own data)
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78,
80, 81, 82, 83, 82, 80, 78, 76, 74, 71]
plt.plot(days,temperature,"bo-")
plt.title("Daily temperature changes in july")
plt.xlabel("Day of the months")
plt.ylabel("Temperature(F)")

plt.show()