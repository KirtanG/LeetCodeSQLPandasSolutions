import pandas as pd

#Table Schema
data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].apply(str.capitalize)
    users = users.sort_values(by=['user_id'])
    return users

# Problem Link: https://leetcode.com/problems/fix-names-in-a-table/
