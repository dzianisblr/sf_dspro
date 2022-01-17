from collections import deque # Don't forget

""" Решения задач Блока 1. PYTHON-9.  
    Задача 4.3 """   
 
def brackets(line):
    
    # сразу проверим не пустая ли строка, если True - выполнение прекращается
    if line == '':
        return True

    # создадим пустой стек и булевую переменную 
    dq_line = deque()
    dq_bool = False

    # перебираем все элементы строки line
    for each in line:
        
        # если стек пуст и имеем на входе закрывающую скобку, то False
        if len(dq_line) == 0 and each == ')':
            return dq_bool
        # иначе, если скобка открывающая - заносим ее в стек
        elif each == '(':
            dq_line.append(each)
        # иначе (подразумевается на входе закрывающая скобка) - 
        # удаляем последний элемент.
        # Т.е., если стек не пуст, то в нем есть некое количество '('
        # значит закрывающая скобка формирует правильную пару '()'
        else:
            dq_line.pop()
    
    # в конце проверяем, не осталось ли незакрытых скобок (пуст ли стек)
    if len(dq_line) == 0:
        dq_bool = True

    return dq_bool


# ПРОВЕРКА
print(brackets('(()())()(())'))
print(brackets(''))
print(brackets('(()(())'))


