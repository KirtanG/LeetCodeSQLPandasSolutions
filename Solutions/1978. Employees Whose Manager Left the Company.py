import pandas as pd

#Table Schema
data = [[3, 'Mila', 9, 60301], [12, 'Antonella', None, 31000], [13, 'Emery', None, 67084], [1, 'Kalel', 11, 21241], [9, 'Mikaela', None, 50937], [11, 'Joziah', 6, 28485]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'manager_id', 'salary']).astype({'employee_id':'Int64', 'name':'object', 'manager_id':'Int64', 'salary':'Int64'})

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.loc[(employees['salary'] < 30_000) & ~employees['manager_id'].isin(employees['employee_id']) & (~employees["manager_id"].isnull())]
    df = df.sort_values(by="employee_id",ascending=True)
    return df[['employee_id']]


# Problem Link:https://leetcode.com/problems/employees-whose-manager-left-the-company/
