import pandas as pd

#Table Schema
data = [[1, 'Avengers'], [2, 'Frozen 2'], [3, 'Joker']]
movies = pd.DataFrame(data, columns=['movie_id', 'title']).astype({'movie_id':'Int64', 'title':'object'})
data = [[1, 'Daniel'], [2, 'Monica'], [3, 'Maria'], [4, 'James']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
data = [[1, 1, 3, '2020-01-12'], [1, 2, 4, '2020-02-11'], [1, 3, 2, '2020-02-12'], [1, 4, 1, '2020-01-01'], [2, 1, 5, '2020-02-17'], [2, 2, 2, '2020-02-01'], [2, 3, 2, '2020-03-01'], [3, 1, 3, '2020-02-22'], [3, 2, 4, '2020-02-25']]
movie_rating = pd.DataFrame(data, columns=['movie_id', 'user_id', 'rating', 'created_at']).astype({'movie_id':'Int64', 'user_id':'Int64', 'rating':'Int64', 'created_at':'datetime64[ns]'})

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    person = pd.merge(left=users,right=movie_rating,on='user_id',how='inner')
    person = person.groupby(by=['user_id','name']).count().reset_index().sort_values(['rating','name'],ascending=[False,True])
    person = person.reset_index()
    person = person['name'][0]
    movie = pd.merge(left=movies,right=movie_rating,on='movie_id',how='inner')
    movie = movie[movie['created_at'].dt.to_period('M') == '2020-02']
    movie = movie.groupby(by=['movie_id','title']).mean().reset_index().sort_values(['rating','title'],ascending=[False,True])
    movie = movie.reset_index()
    movie = movie['title'][0]
    
    result = pd.DataFrame(data=[person,movie],columns = ['results'])
    return result

# Problem Link: https://leetcode.com/problems/movie-rating/
