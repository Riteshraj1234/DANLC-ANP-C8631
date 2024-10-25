# Suppose you work for a retail company, and you have dummy data containing sales
# data for the past year. The data includes information such as SalesDate,product
# names,regions, sales quantities, prices, and dates. You have to generate a bar chart,pie plot on region and prices and
# line chart on SalesDate and prices columns.# Further, you need to get some inference out of the chart.
# Create a ChatGPT prompt to generate the code for this scenario. Based on the code generated, ask ChatGPT to give the conclusion/inference.
# Note. You can provide the data to ChatGPT or ask it to use sample data.
from matplotlib import pyplot as plt

sales_dates = ['2023-01-31', '2023-01-31', '2023-02-28', '2023-02-28','2023-03-31', '2023-03-31', '2023-04-30', '2023-04-30',
    '2023-05-31', '2023-05-31']
products = ['Electronics', 'Clothing', 'Home & Garden', 'Sports & Outdoors','Electronics', 'Clothing', 'Home & Garden', 'Sports & Outdoors',
    'Electronics', 'Clothing']
regions = ['North', 'East', 'South', 'West','North', 'East', 'South', 'West','North', 'East']
quantities = [30, 20, 15, 25, 22, 18, 10, 28, 35, 25]
prices = [150.00, 80.00, 120.00, 100.00,170.00, 90.00, 130.00, 110.00,155.00, 90.00]
total_sales = [4500.00, 1600.00, 1800.00, 2500.00,3740.00, 1620.00, 1300.00, 3080.00,5425.00, 2250.00]

fig , axs=plt.subplots(2,2,figsize =(10,7))

axs[0, 0].bar(regions,prices)
axs[0, 0].set_title("Prices in Different Regions")
axs[0, 0].set_ylabel("Prices ")
axs[0, 0].set_xlabel("Regions")

axs[0, 1].pie(prices, labels=regions,)
axs[0, 1].set_title("Total Prices in Different Regions")


axs[1, 0].plot(sales_dates, total_sales)
axs[1, 0].set_title("Date Wise Sales")
axs[1, 0].set_xlabel('Dates')
axs[1, 0].set_ylabel("Sales price")

axs[1, 1].bar(products,quantities)
axs[1, 1].set_title("Product per Quantity")
axs[1, 1].set_xlabel("Product")
axs[1, 1].set_ylabel('Quantity')

plt.tight_layout
plt.show()



