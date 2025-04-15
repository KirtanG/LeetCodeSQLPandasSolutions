import pandas as pd

#Table Schema
data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15], [2, '2019-02-21', '2019-03-31', 30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype({'product_id':'Int64', 'start_date':'datetime64[ns]', 'end_date':'datetime64[ns]', 'price':'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype({'product_id':'Int64', 'purchase_date':'datetime64[ns]', 'units':'Int64'})

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(left = prices,right = units_sold,on= 'product_id',how = 'left')
    df = df[(df['purchase_date'].isna())| (df['purchase_date'] >= df['start_date']) & (df['purchase_date'] <= df['end_date'])]
    average_price = df.groupby('product_id').apply(lambda x: (x['price'] * x['units']).sum() / x['units'].sum())
    average_price = average_price.fillna(0).round(2)
    df = pd.DataFrame({'product_id': average_price.index, 'average_price': average_price.values})
    return df 

# Problem Link: https://leetcode.com/problems/average-selling-price/description/ 
