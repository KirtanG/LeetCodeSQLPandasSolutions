import pandas as pd

#Table Schema
data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
visits = pd.DataFrame(data, columns=['visit_id', 'customer_id']).astype({'visit_id':'Int64', 'customer_id':'Int64'})
data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
transactions = pd.DataFrame(data, columns=['transaction_id', 'visit_id', 'amount']).astype({'transaction_id':'Int64', 'visit_id':'Int64', 'amount':'Int64'})

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(visits,transactions,on="visit_id",how="left")
    df = df[df['transaction_id'].isna()]
    df = df.groupby("customer_id",as_index = False)
    df = df.agg(count_no_trans=('visit_id', 'nunique'))
    return df


# Problem Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions