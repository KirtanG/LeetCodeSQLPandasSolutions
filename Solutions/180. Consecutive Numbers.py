import pandas as pd

#Table Schema
data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['prev1'] = logs['num'].shift(1)
    logs['prev2'] = logs['num'].shift(2)
    consecutive = logs[(logs['num'] == logs['prev1']) & (logs['num'] == logs['prev2'])]
    consecutive = consecutive['num'].unique()
    df = pd.DataFrame({"ConsecutiveNums":consecutive})
    return df

# Problem Link:https://leetcode.com/problems/consecutive-numbers/
