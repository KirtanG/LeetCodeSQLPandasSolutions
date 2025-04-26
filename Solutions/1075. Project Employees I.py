import pandas as pd

#Table Schema
data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype({'project_id':'Int64', 'employee_id':'Int64'})
data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype({'employee_id':'Int64', 'name':'object', 'experience_years':'Int64'})

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df =  pd.merge(left = project,right = employee ,on = 'employee_id',how = 'left')
    avg = df[['project_id','experience_years']].groupby('project_id').mean()  
    avg = avg.reset_index()
    avg = avg.rename(columns={"experience_years":"average_years"})
    avg['average_years']=avg['average_years'].round(2)
    return avg


# Problem Link: https://leetcode.com/problems/project-employees-i/ 
