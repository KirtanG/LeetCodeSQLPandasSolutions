import pandas as pd

#Table Schema
data = [[1, 'Jhon', '2019-01-01', 100], [2, 'Daniel', '2019-01-02', 110], [3, 'Jade', '2019-01-03', 120], [4, 'Khaled', '2019-01-04', 130], [5, 'Winston', '2019-01-05', 110], [6, 'Elvis', '2019-01-06', 140], [7, 'Anna', '2019-01-07', 150], [8, 'Maria', '2019-01-08', 80], [9, 'Jaze', '2019-01-09', 110], [1, 'Jhon', '2019-01-10', 130], [3, 'Jade', '2019-01-10', 150]]
customer = pd.DataFrame(data, columns=['customer_id', 'name', 'visited_on', 'amount']).astype({'customer_id':'Int64', 'name':'object', 'visited_on':'datetime64[ns]', 'amount':'Int64'})

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.sort_values("visited_on").groupby("visited_on")[["amount"]].sum()
    df = df.assign(amount = df.rolling("7D").sum(), average_amount = round(df.rolling("7D").sum()/7,2))
    return df.loc[df.index >= df.index.min() + pd.DateOffset(6)].reset_index()

# Problem Link:https://leetcode.com/problems/restaurant-growth/
