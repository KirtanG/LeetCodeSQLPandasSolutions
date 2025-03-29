import pandas as pd

#Table Schema
data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    id_df = employee.groupby('managerId').size()
    id_df = id_df[lambda x:x >= 5].index
    df = employee[employee['id'].isin(id_df)] 
    return df[['name']]

# Problem Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
