import pandas as pd

#Table Schema
data = [[0, 95, 100, 105], [1, 70, None, 80]]
products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'Int64', 'store1':'Int64', 'store2':'Int64', 'store3':'Int64'})


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = pd.melt(products,id_vars=['product_id'],value_vars=["store1","store2","store3"])
    result = result.dropna()
    result = result.rename(columns={"variable":"store","value":"price"})
    return result

# Problem Link: https://leetcode.com/problems/rearrange-products-table/