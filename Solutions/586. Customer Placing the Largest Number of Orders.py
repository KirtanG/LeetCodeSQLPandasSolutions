import pandas as pd

#Table Schema
data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number').size()
    result = df.idxmax()
    return pd.DataFrame({'customer_number': [result]})

# Problem Link: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/