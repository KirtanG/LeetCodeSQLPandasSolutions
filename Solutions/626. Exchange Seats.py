import pandas as pd

#Table Schema
data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']]
seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id':'Int64', 'student':'object'})

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    length = len(seat.index)
    temp = seat["student"].copy()
    for i in range(length):
        if i % 2 == 1:
            seat.loc[i,"student"] = temp[i - 1]
        else:
            seat.loc[i,"student"] = temp[(i+1) % length]
    if length % 2:
        seat.loc[length - 1, "student"] = temp[length - 1]
    return seat

# Problem Link: https://leetcode.com/problems/exchange-seats/
