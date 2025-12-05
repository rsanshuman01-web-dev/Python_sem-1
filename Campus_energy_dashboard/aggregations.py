import pandas as pd

def calculate_daily_totals(df):
    df = df.set_index('timestamp')
    daily = df.groupby('building').resample('D')['kwh'].sum().reset_index()
    return daily

def calculate_weekly_aggregates(df):
    df = df.set_index('timestamp')
    weekly = df.groupby('building').resample('W')['kwh'].sum().reset_index()
    return weekly

def building_wise_summary(df):
    summary = []

    for building, group in df.groupby("building"):
        total = group['kwh'].sum()
        mean = group['kwh'].mean()
        mx = group['kwh'].max()
        mn = group['kwh'].min()

        summary.append({
            "building": building,
            "total_kwh": total,
            "mean_kwh": mean,
            "min_kwh": mn,
            "max_kwh": mx
        })

    return pd.DataFrame(summary)
