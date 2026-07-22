import pandas as pd

#Table Schema
data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers,orders,left_on='id',right_on='customerId',how='left')
    df = df[df['customerId'].isna()].rename(columns={'name':'Customers'})
    return df[['Customers']]

# Problem Link: https://leetcode.com/problems/customers-who-never-order/
