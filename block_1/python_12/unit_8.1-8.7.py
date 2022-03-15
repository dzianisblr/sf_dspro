from asyncio import as_completed
import pandas as pd
import re

rating_movies = pd.read_csv('block_1/python_12/data/ratings_movies.csv')

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None
    

rating_movies['year_release'] = rating_movies['title'].apply(get_year_release)

mask = rating_movies['year_release'] == 2018 # для задачи 8.2=1999, 8.3=2010, 8.6=2018
min_rate_movie = rating_movies[mask].groupby('title')['rating'].mean().sort_values()
min_rate_genres = rating_movies[mask].groupby('genres')['rating'].mean().sort_values()
user_max_unique_genres = rating_movies.groupby('userId')['genres'].nunique().sort_values()
min_activity_user = rating_movies.groupby('userId')\
    ['rating'].agg(['count', 'mean']).sort_values(by=['count', 'mean'], ascending=[True,False])
max_rate_genres = rating_movies[mask].groupby('genres')\
    ['rating'].agg(['mean', 'count']).sort_values(by=['count', 'mean'], ascending=[False,False])

rating_movies['year_rating'] = pd.to_datetime(rating_movies['date']).dt.year
meanrate_by_year = rating_movies.pivot_table(
    values='rating',
    index='genres',
    columns='year_rating',
    aggfunc='mean',
    fill_value=0
)

print(meanrate_by_year.loc['Comedy'].round(2))


#print(min_rate_movie.head(1))
#print(min_rate_genres.head(1))
#print(user_max_unique_genres)
#print(min_activity_user.head(1))
#print(max_rate_genres.head(5))
#print(rating_movies['date'].head(1))