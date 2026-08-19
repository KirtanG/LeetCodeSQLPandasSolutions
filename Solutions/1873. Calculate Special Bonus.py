import pandas as pd

#Table Schema
data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.copy().apply(
        lambda row: 0 if(row['employee_id'] % 2 == 0) or str(row['name']).upper().startswith('M') else row['salary'], axis = 1
    )
    return employees[['employee_id','bonus']].sort_values('employee_id')


# Problem Link: https://leetcode.com/problems/calculate-special-bonus/