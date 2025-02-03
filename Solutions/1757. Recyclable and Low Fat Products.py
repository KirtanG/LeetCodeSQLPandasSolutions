import pandas as pd

#Table Schema
data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    product = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return product[['product_id']]

# Problem Link: https://leetcode.com/problems/recyclable-and-low-fat-products	
