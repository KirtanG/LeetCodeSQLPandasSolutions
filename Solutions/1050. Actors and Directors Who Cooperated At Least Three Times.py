import pandas as pd

#Table Schema
data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    """SELECT
    actor_id,director_id
FROM
    ActorDirector 
GROUP BY
    actor_id,director_id
HAVING COUNT(*) >=3; """
    # Group the data by actor_id and director_id, and count the number of cooperations
    grouped = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
    
    # Filter the pairs where the cooperation count is at least three
    filtered_pairs = grouped[grouped['cooperation_count'] >= 3]
    
    return filtered_pairs[['actor_id', 'director_id']]

# Problem Link: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times
