from collections import Counter, OrderedDict
from block_1.python_9.hidden import north, center, south


def shop_sells(shop):
    
    products_list = []
    
    for each in shop:
        products_list.extend(each)
    
    return products_list


shopsale_dict = {'north': shop_sells(north),\
                'center': shop_sells(center),\
                'south': shop_sells(south)
                }

max_sales_shop_name = ''
max_sales = 0

for each in shopsale_dict:
    sales = Counter(shopsale_dict[each])
    #print(each, ':', sales, ' - all ', sum(sales.values()))
    
    if sum(sales.values()) > max_sales:
        max_sales = sum(sales.values())
        max_sales_shop_name = each
        

print('Unit 9.4.4 - ', max_sales_shop_name, ' : ', max_sales)

north_notpopular_sale = Counter(shopsale_dict['north']).most_common()
print('Unit 9.4.5 - ', north_notpopular_sale[-1][0], ' : ', north_notpopular_sale[-1][1])

sales_lst = ['Bread', 'Yoghurt', 'Beer', 'Cola']
search_sale = ''
sales_center = Counter(shopsale_dict['center'])
sales_north = Counter(shopsale_dict['north'])
sales_center.subtract(sales_north)

for each in sales_lst:
    if sales_center[each] > 0:
        search_sale = each
        break
    
print(f'Unit 9.4.6 - In center most sales: {search_sale} - {sales_center[search_sale]}')