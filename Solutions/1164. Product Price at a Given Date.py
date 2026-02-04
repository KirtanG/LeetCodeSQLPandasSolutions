import pandas as pd

#Table Schema
data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'], [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype({'product_id':'Int64', 'new_price':'Int64', 'change_date':'datetime64[ns]'})

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
      last_price = products[products['change_date'] <= '2019-08-16'].sort_values(by=['product_id','change_date'],ascending=[True, False]).drop_duplicates(subset=['product_id'],keep='first')
      output = pd.merge(products[['product_id']].drop_duplicates(),last_price[['product_id','new_price']],how='left').fillna(10).rename(columns={'new_price':'price'})
      return output 

# Problem Link:https://leetcode.com/problems/product-price-at-a-given-date/