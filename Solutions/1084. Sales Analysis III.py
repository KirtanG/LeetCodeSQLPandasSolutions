import pandas as pd

#Table Schema
data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype({'product_id':'Int64', 'product_name':'object', 'unit_price':'Int64'})
data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800], [3, 3, 4, '2019-05-13', 2, 2800]]
sales = pd.DataFrame(data, columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype({'seller_id':'Int64', 'product_id':'Int64', 'buyer_id':'Int64', 'sale_date':'datetime64[ns]', 'quantity':'Int64', 'price':'Int64'})

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    start = '2019-01-01'
    end = '2019-03-31'
    
    # Mimic the sub-query
    sales_outside_range = sales[
        (sales['sale_date'] < start) |
        (sales['sale_date'] > end)
    ]

    sales_inside_range = sales[
        (sales['sale_date'] >= start) |
        (sales['sale_date'] <= end)
    ]
    

    invalid_ids = sales_outside_range["product_id"].unique() 

    valid_products = sales_inside_range[
    ~sales_inside_range['product_id'].isin(invalid_ids)
]
    result = product[
    product['product_id'].isin(valid_products['product_id'].unique())
][['product_id', 'product_name']]

    return result


# Problem Link: https://leetcode.com/problems/sales-analysis-iii/