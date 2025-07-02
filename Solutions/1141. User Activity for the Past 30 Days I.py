import pandas as pd

#Table Schema
data = [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'], [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'], [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'], [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'], [3, 2, '2019-07-21', 'end_session'], [4, 3, '2019-06-25', 'open_session'], [4, 3, '2019-06-25', 'end_session']]
activity = pd.DataFrame(data, columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype({'user_id':'Int64', 'session_id':'Int64', 'activity_date':'datetime64[ns]', 'activity_type':'object'})

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity[(activity['activity_date'] <= '2019-07-27') & (activity['activity_date'] > pd.to_datetime('2019-07-27') - pd.Timedelta(days = 30))  ]
    df = df.groupby('activity_date').nunique().reset_index()
    df = df.rename(columns={'activity_date':'day','user_id':'active_users'}).sort_values('day')
    return df[["day","active_users"]]


# Problem Link: https://leetcode.com/problems/user-activity-for-the-past-30-days-i/