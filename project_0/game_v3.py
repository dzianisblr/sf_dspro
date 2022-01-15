import numpy as np

def random_predict(number: int=1)->int: # функция угадывания
    
    count = 0
    max_num = 101
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
        
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости - вот тут пока непонятно
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    #print(random_array) # можно просмотреть массив сгенерированных чисел - для лучшего понимания процесса
    
    for number in random_array: # для каждого из сгенерированных чисел 
        count_ls.append(random_predict(number)) # через вызов функции угадывания формируем массив попыток

    #print(count_ls) # можно просмотреть массив попыток - для лучшего понимания процесса
    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')

# RUN
score_game(random_predict)