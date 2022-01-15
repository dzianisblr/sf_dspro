import numpy as np

 
def random_predict(number: int=1)->int: # функция угадывания

    count = 0
    max_num = 100
    min_num = 1

    while True:
        count += 1
        finding_num = (max_num + min_num) // 2 # медиана для уменьшения вариантов в 2 раза
        
        if number == finding_num: # пробуем угадать
            break
        elif number > finding_num: # если загаданное больше
            min_num = finding_num # следующим проходом начнем поиск от предположенного в большую сторону
        else:
            max_num = finding_num # иначе, в меньшую
    
    print(f'Find! {finding_num}')
    
    return count

print(random_predict(99))