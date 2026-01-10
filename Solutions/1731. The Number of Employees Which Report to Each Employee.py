import pandas as pd

#Table Schema
data = [[9, 'Hercy', None, 43], [6, 'Alice', 9, 41], [4, 'Bob', 9, 36], [2, 'Winston', None, 37]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'reports_to', 'age']).astype({'employee_id':'Int64', 'name':'object', 'reports_to':'Int64', 'age':'Int64'})

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(left=employees,right=employees,left_on = 'employee_id',right_on='reports_to')
    merged_df = merged_df.groupby(['employee_id_x','name_x']).agg(reports_count=('name_y','count'),average_age=('age_y','mean')).reset_index()
    merged_df['average_age'] = (merged_df['average_age'] + 0.01).round() 
    merged_df = merged_df.rename(columns={'employee_id_x':'employee_id','name_x':'name'})
    return merged_df

# Problem Link: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/ 