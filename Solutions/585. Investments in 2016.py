import pandas as pd

#Table Schema
data = [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]
insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype({'pid':'Int64', 'tiv_2015':'Float64', 'tiv_2016':'Float64', 'lat':'Float64', 'lon':'Float64'})

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    unique_latlon = insurance.drop_duplicates(subset=['lat','lon'],keep=False)['pid']
    duplicates = insurance.loc[insurance.duplicated(subset='tiv_2015',keep=False)]['pid']
    df = insurance.loc[insurance['pid'].isin(unique_latlon) & insurance['pid'].isin(duplicates)]
    return df[['tiv_2016']].sum().to_frame('tiv_2016').round(2) 

# Problem Link:https://leetcode.com/problems/investments-in-2016/