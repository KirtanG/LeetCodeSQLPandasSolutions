import pandas as pd

#Table Schema
data = [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']]
users = pd.DataFrame(data, columns=['user_id', 'user_name']).astype({'user_id':'Int64', 'user_name':'object'})
data = [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2], [207, 2], [210, 7]]
register = pd.DataFrame(data, columns=['contest_id', 'user_id']).astype({'contest_id':'Int64', 'user_id':'Int64'})

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df  = register.groupby('contest_id').count()['user_id']
    df = df.apply(lambda x: (x/len(users['user_id'].unique())*100))
    df = df.round(2).reset_index()
    df = df.rename(columns={'user_id':'percentage'})
    df = df.sort_values(by = ['percentage','contest_id'],ascending = [False,True])
    return df


# Problem Link: https://leetcode.com/problems/percentage-of-users-attended-a-contest/ 
