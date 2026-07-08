import pandas as pd

#Table Schema
data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset=['salary'],inplace=True)
    if len(employee) < N or N <= 0 :
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    employee['dense_rank'] = employee['salary'].rank(method='dense',ascending=False)
    result = employee[employee['dense_rank'] == N]['salary'].iloc[0]
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})

# Problem Link: https://leetcode.com/problems/nth-highest-salary/
