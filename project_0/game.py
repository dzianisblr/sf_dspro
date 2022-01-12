import numpy as np
from numpy.random.mtrand import randint

number = np.random.randint(1,101)
count = 0

while True:
    count += 1
    current_num = int(input('Угадай число от 1 до 100: '))
    if current_num > number:
        print('Число должно быть меньше')
    elif current_num < number:
        print('Число должно быть больше')
    else:
        print(f'Вы угадали число {number} с {count}-й попытки')
        break
       
