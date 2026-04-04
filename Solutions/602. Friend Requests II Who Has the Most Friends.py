import pandas as pd

#Table Schema
data = [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']]
request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype({'requester_id':'Int64', 'accepter_id':'Int64', 'accept_date':'datetime64[ns]'})

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([request_accepted['requester_id'],request_accepted['accepter_id']],axis=0).to_frame('id')
    df = df.groupby(by='id',as_index=False).agg(num=('id','count')).sort_values(by='num',ascending=False)
    return df.head(1)

# Problem Link: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
