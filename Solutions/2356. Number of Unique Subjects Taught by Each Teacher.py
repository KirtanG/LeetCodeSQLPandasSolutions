import pandas as pd

#Table Schema
data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(by="teacher_id").nunique() # use nunique to count unique values 
    df =  df.reset_index().rename(columns={"subject_id":"cnt"})
    return df[['teacher_id',"cnt"]]

# Problem Link:https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher
