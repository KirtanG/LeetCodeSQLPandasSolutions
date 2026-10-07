import pandas as pd

#Table Schema
data = [[1, 'alice@example.com'], [2, 'bob_at_example.com'], [3, 'charlie@example.net'], [4, 'david@domain.com'], [5, 'eve@invalid']]
users = pd.DataFrame(columns=["user_id", "email"]).astype({"user_id": "int32", "email": "string"})


def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
    df = users[users['email'].str.match(regex)].sort_values("user_id")
    return df

# Problem Link: https://leetcode.com/problems/find-valid-emails/