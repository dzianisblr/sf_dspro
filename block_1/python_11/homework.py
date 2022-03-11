import pandas as pd
#import numpy as np

"""
ufo_db = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')
#print(ufo_db.head(10))
#print(ufo_db.info())

ufo_db['Time'] = pd.to_datetime(ufo_db['Time'])
#print(ufo_db['Time'].head())
ufo_year = ufo_db['Time'].dt.year
print(ufo_year.mode()[0])

ufo_nevada = ufo_db[ufo_db['State']=='NV']
ufo_nevada['Date'] = ufo_nevada['Time'].dt.date
days_between = ufo_nevada['Date'].diff().dt.days
print(days_between)
print(days_between.mean())
"""
bike_data = pd.read_csv('block_1\python_11\data\citibike-tripdata.csv')
bike_db = bike_data.copy()
print(bike_db.head())


