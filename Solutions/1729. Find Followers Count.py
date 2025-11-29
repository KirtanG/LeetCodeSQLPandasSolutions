import pandas as pd

#Table Schema
data = [['0', '1'], ['1', '0'], ['2', '0'], ['2', '1']]
followers = pd.DataFrame(data, columns=['user_id', 'follower_id']).astype({'user_id':'Int64', 'follower_id':'Int64'})

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df = followers.groupby("user_id").count().reset_index()
    df = df.rename(columns={"follower_id":"followers_count"})
    return df

# Problem Link: https://leetcode.com/problems/find-followers-count/