import pandas as pd

#Table Schema
data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1], ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype({'query_name':'object', 'result':'object', 'position':'Int64', 'rating':'Int64'})


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating']/queries['position'] + 1e-10
    queries['poor_query_percentage'] = queries.apply(lambda x: 100 if x['rating'] < 3 else 0, axis=1)
    return queries[['query_name','quality','poor_query_percentage']].groupby(['query_name'],as_index=False)[['quality','poor_query_percentage']].mean().round(2)

# Problem Link: https://leetcode.com/problems/queries-quality-and-percentage/ 
