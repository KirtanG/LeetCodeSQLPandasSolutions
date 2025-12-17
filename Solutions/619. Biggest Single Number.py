import pandas as pd

#Table Schema
data = [[8], [8], [3], [3], [1], [4], [5], [6]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.value_counts().reset_index()
    df = df[df["count"] == 1]
    result = df["num"].max()
    return pd.DataFrame([result],columns=['num'])

# Problem Link: https://leetcode.com/problems/biggest-single-number/