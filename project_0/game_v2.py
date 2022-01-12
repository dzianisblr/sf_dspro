import numpy as np

#if __name__ == '__main__':
    
def random_predict(number: int=1)->int:
    
    count = 0
    
    while True:
        count += 1
        
        if number == np.random.randint(1,101):

            break
    return count # ,number - для _list
#print(f'Число {_list[1]} угадано, попыток - {_list[0]}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    #print(random_array)
    
    for number in random_array:
        count_ls.append(random_predict(number))

    #print(count_ls)
    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    #return(score)

# RUN
score_game(random_predict)