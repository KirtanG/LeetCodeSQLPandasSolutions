import pandas as pd

#Table Schema
data = [['1', '1', 'N'], ['2', '1', 'Y'], ['2', '2', 'N'], ['3', '3', 'N'], ['4', '2', 'N'], ['4', '3', 'Y'], ['4', '4', 'N']]
employee = pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag']).astype({'employee_id':'Int64', 'department_id':'Int64', 'primary_flag':'object'})

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    single_department_emp = employee['employee_id'].value_counts()[employee['employee_id'].value_counts()== 1].index
    df = employee[(employee['employee_id'].isin(single_department_emp))|(employee['primary_flag'] == 'Y')]
    return df[['employee_id','department_id']] 


# Problem Link: https://leetcode.com/problems/primary-department-for-each-employee/ 