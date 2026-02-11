import pandas as pd

#Table Schema
data = [[5, 'Alice', 250, 1], [4, 'Bob', 175, 5], [3, 'Alex', 350, 2], [6, 'John Cena', 400, 3], [1, 'Winston', 500, 6], [2, 'Marie', 200, 4]]
queue = pd.DataFrame(data, columns=['person_id', 'person_name', 'weight', 'turn']).astype({'person_id':'Int64', 'person_name':'object', 'weight':'Int64', 'turn':'Int64'})

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values("turn")
    queue['running_sum'] = queue['weight'].cumsum() #cumsum for cumlative sum
    df = queue[queue['running_sum'] <= 1000].tail(1)
    return df[['person_name']]

# Problem Link:https://leetcode.com/problems/last-person-to-fit-in-the-bus
