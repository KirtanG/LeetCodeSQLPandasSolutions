import pandas as pd

#Table Schema
data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby(by='product_id')['year'].min().reset_index()
    sales = pd.merge(left = sales , right = df , how='inner', on=['product_id','year'])
    df = sales.rename(columns={"year":"first_year"})
    return df[["product_id","first_year","quantity","price"]]

# Problem Link: https://leetcode.com/problems/product-sales-analysis-iii 
