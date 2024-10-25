# Lab4: Suppose you're a sales manager for an e-commerce company, and you
# want to create a figure with subplots to compare the sales performance of
# different product categories over time. You have sales data for four product
#categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share
# your conclusion/analysis.
# Input:
import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

fig , axs=plt.subplots(2,2,figsize =(10,10))

axs[0, 0].plot(months, electronics_sales,"bo-")
axs[0, 0].set_title('Electronics')
axs[0, 0].set_ylabel('Sales Amount')
axs[0, 0].set_xlabel('Month ')

axs[0, 1].plot(months, clothing_sales,"go-")
axs[0, 1].set_title('Clothing')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Sales Amount')

axs[1, 0].plot(months, home_garden_sales,"ro-")
axs[1, 0].set_title('Home & Garden')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Sales Amount')

axs[1, 1].plot(months, sports_outdoors_sales,"mo-")
axs[1, 1].set_title('Sports & Outdoors')
axs[1, 1].set_xlabel('Month')
axs[1, 1].set_ylabel('Sales Amount')

plt.tight_layout
plt.show()

