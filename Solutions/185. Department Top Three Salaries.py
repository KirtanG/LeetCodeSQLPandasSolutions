import pandas as pd

#Table Schema
data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1], [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(left=employee,right=department,left_on = 'departmentId',right_on = 'id',how='left')
    df = df[df.groupby('departmentId')['salary'].rank(method='dense',ascending = False) <= 3]
    df = df[['name_y', 'name_x', 'salary']].rename(columns = {'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    return df

# Problem Link: https://leetcode.com/problems/department-top-three-salaries/
