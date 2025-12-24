import pandas as pd

#Table Schema
data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype({'customer_id':'Int64', 'product_key':'Int64'})
data = [[5], [6]]
product = pd.DataFrame(data, columns=['product_key']).astype({'product_key':'Int64'})

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    count_df = product.count()
    df = customer.groupby('customer_id').nunique()
    df = df[df["product_key"] == count_df[0]]
    df = df.reset_index()[['customer_id']]
    # print(df.reset_index())
    return df

# Problem Link: https://leetcode.com/problems/customers-who-bought-all-products 
