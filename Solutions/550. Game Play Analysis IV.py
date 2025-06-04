import pandas as pd

#Table Schema
data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first"] = activity.groupby("player_id").event_date.transform(min)
    df = activity.loc[activity["first"] + pd.DateOffset(1) == activity["event_date"]]
    fraction = round(len(df)/activity.player_id.nunique(),2)
    result = pd.DataFrame(data=[fraction],columns=["fraction"])
    return result

# Problem Link: https://leetcode.com/problems/game-play-analysis-iv/