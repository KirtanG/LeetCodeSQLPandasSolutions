import pandas as pd

#Table Schema
data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
   df = courses.groupby('class')['student'].count()
   df = df[df>=5].index
   return pd.DataFrame({"class":df}) 

# Problem Link: https://leetcode.com/problems/classes-with-at-least-5-students/