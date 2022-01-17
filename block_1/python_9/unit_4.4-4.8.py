from collections import Counter # Don't forget
from hidden import north, center, south

""" Решения задач Блока 1. PYTHON-9.  """
  
# избавимся от лишней вложенности [[...],...,[...],...]
# для этого создадим функцию, чтобы не писать код для каждого магазина
def shop_sells(shop):
    
    products_list = []
    
    for each in shop:
        products_list.extend(each)
    
    return products_list

# создадим словарь со списком всех покупок для каждого магазина
# он нам пригодится еще и в последующих задачах
shopsale_dict = {'north': shop_sells(north),\
                'center': shop_sells(center),\
                'south': shop_sells(south)
                }


""" Задача 4.4 """ 

# объявим переменные, где будем хранить название магазина и количество продаж
max_sales_shop_name = ''
max_sales = 0

# переберем по очереди из словаря данные по каждому магазину
for each in shopsale_dict:
    # создадим счетчик всех продуктов в каждом магазине
    sales = Counter(shopsale_dict[each])
    
    # ищем магазин с максимальным количеством продаж всего
    if sum(sales.values()) > max_sales:
        max_sales = sum(sales.values())
        max_sales_shop_name = each
        
# выводим результат
print(f'Unit 9.4.4 - {max_sales_shop_name} : {max_sales}')


"""    Задача 4.5    """ 

# создаем опять счетчик товаров, но с учетом убывания продаж
north_notpopular_sale = Counter(shopsale_dict['north']).most_common()

# выводим данные по последнему товару - наименьшие продажи
print('Unit 9.4.5 - ', north_notpopular_sale[-1][0], ' : ', north_notpopular_sale[-1][1])


"""    Задача 4.6    """ 

# Создадим список товаров для сравнения, зададим переменную для искомого товара
sales_lst = ['Bread', 'Yoghurt', 'Beer', 'Cola']
search_sale = ''
# подсчитаем продажу товаров по каждому магазину
# удалим продажи одного магазина из другого
sales_center = Counter(shopsale_dict['center'])
sales_north = Counter(shopsale_dict['north'])
sales_center.subtract(sales_north)

# проверим, каких товаров из списка искомых, осталось положительное количество
# предполагается, что такой товар один
for each in sales_lst:
    if sales_center[each] > 0:
        search_sale = each
        break

# выводим результат
print(f'Unit 9.4.6 - In center most sales: {search_sale} - {sales_center[search_sale]}')


"""    Задача 4.7    """ 


