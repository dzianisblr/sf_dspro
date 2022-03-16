from numpy import NaN
import pandas as pd

orders = pd.read_csv('block_1/python_12/data/orders.csv', sep=';')
products = pd.read_csv('block_1/python_12/data/products.csv', sep=';')

orders_products = orders.join(
    products.set_index('Product_ID'),
    on='ID товара',
    how='left'
)

#print(orders_products.tail(3))
print(orders_products[orders_products['Name'].isnull()].loc[:, 'Order ID'])
#print(orders_products[orders_products['Отменен']=='Да'].loc[:, 'Name'])

orders_products['Прибыль'] = orders_products['Количество']\
    * orders_products['Price']
bestbyer = orders_products[orders_products['Оплачен']=='Да']\
    .groupby('ID Покупателя')['Прибыль'].sum()
#print(bestbyer)

#print(products.head())