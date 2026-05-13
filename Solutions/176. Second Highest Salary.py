import pandas as pd

#Table Schema
data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates()
    if len(salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    result = salaries.nlargest(2).iloc[-1]
    return pd.DataFrame({'SecondHighestSalary':[result]})

# Problem Link: https://leetcode.com/problems/second-highest-salary
