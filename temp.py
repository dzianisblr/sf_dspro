word_list = ['My', 'name', 'is', 'Denis']
sentence = ''

for list in word_list:
        print('Current list', list) #выводим текущее значение переменной list
        print('Current sentence', sentence) #выводим текущее значение переменной sentence
        sentence += list #увеличиваем сумму фразы на значение list, равносильно sentence = sentence + list
        print('New sentence', sentence) #выводим обновлённое значение переменной sentence
        print() #выводим пустую строку для красивого отображения
print('Answer: sentence=', sentence) #выводим результат