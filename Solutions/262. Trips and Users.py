import pandas as pd

#Table Schema
data = [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']]
trips = pd.DataFrame(data, columns=['id', 'client_id', 'driver_id', 'city_id', 'status', 'request_at']).astype({'id':'Int64', 'client_id':'Int64', 'driver_id':'Int64', 'city_id':'Int64', 'status':'object', 'request_at':'object'})

data = [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']]
users = pd.DataFrame(data, columns=['users_id', 'banned', 'role']).astype({'users_id':'Int64', 'banned':'object', 'role':'object'})

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    result = (
    trips
    # left join with Users on client_id
    .merge(users, left_on='client_id', right_on='users_id', how='left', suffixes=('', '_client'))
    # left join with Users again on driver_id
    .merge(users, left_on='driver_id', right_on='users_id', how='left', suffixes=('_client', '_driver'))
    # apply SQL WHERE filters
    .loc[
        lambda df: (
            (df['banned_client'] == 'No')
            & (df['banned_driver'] == 'No')
            & df['request_at'].between('2013-10-01', '2013-10-03')
        )
    ]
    # cancellation flag like CASE WHEN status LIKE 'cancelled%'
    .assign(cancel_flag=lambda df: df['status'].str.startswith('cancelled').astype(float))
    # group and aggregate
    .groupby('request_at', as_index=False)
    .agg(**{"Cancellation Rate": ('cancel_flag', lambda x: round(x.mean(), 2))})
    # rename column for output format
    .rename(columns={'request_at': 'Day'})
)
    return result 

# Problem Link:https://leetcode.com/problems/trips-and-users/
