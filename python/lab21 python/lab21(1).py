# Lab1: Analyze the relationship between the size of houses (measured in square
# footage) and their selling prices in a particular neighborhood. You have collected
# data on various houses in that neighborhood.Create a scatter plot using the
# below data and share your conclusion/analysis.
# Input:
import matplotlib.pyplot as plt
import numpy as np

square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800,
3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

plt.scatter(square_footage,selling_prices)
plt.title("Housing price vs. Square Footage")
plt.xlabel("Square footage (sq.ft.)")
plt.ylabel("Selling price ($000s)")

plt.show()


