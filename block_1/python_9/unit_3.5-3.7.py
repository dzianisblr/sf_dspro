from collections import deque, Counter # Don't forget
from hidden import users

""" Решения задач Блока 1. PYTHON-9.  """   

# создаем очередь/стек
dq_users = deque(users)

""" Задача 3.5 """

print(dq_users.popleft())

""" Задача 3.6 """

dq_users.rotate(-5)
# для использования в следующей задаче создадим переменную с удаляемым элементом
last_el = dq_users.pop()
print(last_el)

""" Задача 3.7 """

# счетчиком создаем словарь {элемент: количество повторений, ...}
# выводим количество из словаря по ключу из задания 3.6 (last_el)
print(Counter(dq_users)[last_el])