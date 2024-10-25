# Suppose you have two columns named regions and sales with some dummy data frame
# and you need to generate a bar chart based on these two columns and also generate the percentage.
# Further, you need to get some inference out of the chart.
# Create a ChatGPT prompt to generate the code for this scenario. Based on the code generated, ask ChatGPT to give the conclusion/inference.
# Note. You can provide the data to ChatGPT or ask it to use sample data.
import matplotlib.pyplot as plt

regions = ['North', 'East', 'South', 'West','North', 'East', 'South', 'West','North', 'East']
total_sales = [4500.00, 1600.00, 1800.00, 2500.00,3740.00, 1620.00, 1300.00, 3080.00,5425.00, 2250.00]

plt.bar(regions,total_sales)

plt.show()
