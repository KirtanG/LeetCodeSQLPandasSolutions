import pandas as pd

#Table Schema
data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how='cross')
    examinations.rename(columns={'subject_name':'subject_name2'},inplace=True)
    df_result=df.merge(examinations, how='left', left_on=['student_id','subject_name'], right_on=['student_id','subject_name2'])
    df_result = df_result.groupby(['student_id','student_name','subject_name'], dropna=False)['subject_name2'].count().reset_index(name='attended_exams')    
    return df_result

# Problem Link: https://leetcode.com/problems/students-and-examinations 
