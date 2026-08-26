import pandas as pd

#Table Schema
data = [[1, '2017-01-01', 10], [2, '2017-01-02', 109], [3, '2017-01-03', 150], [4, '2017-01-04', 99], [5, '2017-01-05', 145], [6, '2017-01-06', 1455], [7, '2017-01-07', 199], [8, '2017-01-09', 188]]
stadium = pd.DataFrame(data, columns=['id', 'visit_date', 'people']).astype({'id':'Int64', 'visit_date':'datetime64[ns]', 'people':'Int64'})

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # filter initial SQL WHERE people >= 100
    df = stadium[stadium['people'] >= 100]
    # replicate exactly what row number does as there is no direct built - in 
    df_cte = df.sort_values(by='id')
    df_cte['row_number'] = df_cte.reset_index().index + 1
    df_cte['diff'] = df_cte['id'] - df_cte['row_number']
    # the cte ends here
    # find diffs that appear at least 3 times
    valid_diffs = df_cte.groupby('diff').filter(lambda g:len(g) >= 3 )['diff'].unique()
    # filter rows where diff is in valid_diffs
    df_cte = df_cte[df_cte['diff'].isin(valid_diffs)]
    return df_cte[['id','visit_date','people']]


# Problem Link: https://leetcode.com/problems/human-traffic-of-stadium/description/