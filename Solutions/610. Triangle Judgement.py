import pandas as pd

#Table Schema
data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x':'Int64', 'y':'Int64', 'z':'Int64'})

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = triangle.apply(isTriangle,axis = 1)
    return triangle


def isTriangle(row:pd.DataFrame) -> str:
    check_1 = row['x'] + row['y'] > row['z']
    check_2 = row['x'] + row['z'] > row['y']
    check_3 = row['z'] + row['y'] > row['x']
    if (check_1 and check_2 and check_3):
        return 'Yes'
    else:
        return 'No'


# Problem Link:https://leetcode.com/problems/triangle-judgement
