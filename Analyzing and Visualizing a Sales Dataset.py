import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')
print(df.head())
df['Date']=pd.to_datetime(df['Date'])
print(df)
total_sales_per_product = df.groupby('Product')['Sales'].sum()
print(total_sales_per_product)

sales = df['Sales'].values

mean_sales=np.mean(sales)
median_sales=np.median(sales)
std_dev_sales = np.std(sales)

print(mean_sales)
print(median_sales)
print(std_dev_sales)

total_sales_per_product.plot(kind='bar',color='skyblue')
plt.title('total sales per product')
plt.xlabel('product')
plt.ylabel('total sales')
plt.show()

plt.figure(figsize=(10,6))
for product in df['Product'].unique():
    product_sales = df[df['Product']==product]
    plt.plot(product_sales['Date'],product_sales['Sales'],marker='o',label=product)

plt.title('sales over time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()