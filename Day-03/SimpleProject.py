import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-02-01', '2024-02-02', '2024-02-03'],
    'Product': ['ML', 'DL', 'Web', 'CP', 'App', 'IT'],
    'Quantity': [10, 5, 8, 7, 3, 12],
    'Price': [200, 100, 130, 113, 150, 200]
}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])


df['Total Sales'] = df['Quantity'] * df['Price']


print("Sample Sales Data:")
print(df)


sales_by_product = df.groupby('Product')['Total Sales'].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)


df['Month'] = df['Date'].dt.to_period('M')  
sales_by_month = df.groupby('Month')['Total Sales'].sum()
print("\nTotal Sales by Month:")
print(sales_by_month)

plt.figure(figsize=(10, 5))
plt.plot(sales_by_month.index.astype(str), sales_by_month.values, marker='o')
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(visible=True)
plt.show()


sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()
