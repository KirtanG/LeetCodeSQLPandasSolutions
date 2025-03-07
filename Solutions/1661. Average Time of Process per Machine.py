import pandas as pd

#Table Schema
def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(left=activity,right=activity,left_on=['machine_id','process_id'],right_on=['machine_id','process_id'],how='inner')
    df = df[df['timestamp_x']<df['timestamp_y']]
    # print(df.head())
    df['diff'] = df['timestamp_y'].sub(df['timestamp_x'],axis=0)
    df_diff = df[['machine_id','diff']].groupby('machine_id').mean()
    df_diff = df_diff.round(3)
    df_diff = df_diff.rename(columns={"diff":'processing_time'})
    return df_diff.reset_index()


# Problem Link: https://leetcode.com/problems/average-time-of-process-per-machine
