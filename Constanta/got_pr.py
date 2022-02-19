from cmath import nan
import pandas as pd
import numpy as np

data = pd.read_excel('F:\SkillFactory\IDE\Constanta\data\dec.xls')

def sells_tbl(got_pr):
    
    """
    jacket = 0 # жакет, жилет 001
    dress = 0  # платье 004
    suit = 0   # костюм 003
    skirt = 0  # юбка 002
    coat = 0   # пальто 005
    other = 0  # прочее 006
    """
    
    for i in range(0, len(got_pr.NAIM)):
        #print(got_pr.NAIM[i])
        
        if got_pr.NAIM[i] is np.nan:
            got_pr.code[i] = '006' # надо не each а его индекс как-то вставить
        elif got_pr.NAIM[i][0] == 'Ж':
            got_pr.code[i] = '001'
        elif got_pr.NAIM[i][0] == 'Ю':
            got_pr.code[i] = '002'
        elif got_pr.NAIM[i][0] == 'К':
            got_pr.code[i] = '003'
        elif got_pr.NAIM[i][:2] == 'Пл':
            got_pr.code[i] = '004'
        elif got_pr.NAIM[i][:2] == 'Па':
            got_pr.code[i] = '005'
        else:
            got_pr.code[i] = '006'
        
    #print(f'Жакеты: {jacket}, Платья: {dress}, Юбки: {skirt}, Костюмы: {suit}, Пальто: {coat}, Прочее: {other}')
    #print(each)
    got_pr.to_excel('./Constanta/data/test.xls')
    print(got_pr.head())
    return None

#print(sells_tbl(data).head())

#sells_tbl(data)

