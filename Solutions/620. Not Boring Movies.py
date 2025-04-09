import pandas as pd

#Table Schema
data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype({'id':'Int64', 'movie':'object', 'description':'object', 'rating':'Float64'})

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[~cinema['description'].str.contains(r'\bboring\b',case=False,regex=True)]
    df = df[df['id'] %2 != 0] 
    df = df.sort_values(by='rating',ascending=False)
    return df

# Problem Link: https://leetcode.com/problems/not-boring-movies/