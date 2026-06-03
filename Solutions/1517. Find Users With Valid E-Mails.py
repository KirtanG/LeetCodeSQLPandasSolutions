import pandas as pd

#Table Schema
data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    result = users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$',na=False)]
    return result

# Problem Link: https://leetcode.com/problems/find-users-with-valid-e-mails/