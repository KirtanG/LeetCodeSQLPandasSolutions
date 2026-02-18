import pandas as pd

#Table Schema
data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    categories = ["Low Salary","Average Salary","High Salary"]
    accountCounts = [len(accounts[accounts['income']<20000]),len(accounts[(accounts['income']>=20000) & (accounts['income']<=50000)]),len(accounts[accounts['income']>50000])]
    result = pd.DataFrame({"category":categories,"accounts_count":accountCounts})
    return result

# Problem Link: https://leetcode.com/problems/count-salary-categories/description/

