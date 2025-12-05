import matplotlib.pyplot as plt

def create_dashboard(daily, weekly, df, out_path="output/dashboard.png"):
    fig, axes = plt.subplots(3, 1, figsize=(12, 14))

    # Trend line (daily)
    for b, g in daily.groupby("building"):
        axes[0].plot(g["timestamp"], g["kwh"], label=b)
    axes[0].set_title("Daily Energy Consumption")
    axes[0].legend()

    # Weekly bar chart
    weekly_avg = weekly.groupby("building")["kwh"].mean()
    axes[1].bar(weekly_avg.index, weekly_avg.values)
    axes[1].set_title("Average Weekly Consumption")

    # Peak scatter
    df['hour'] = df['timestamp'].dt.hour
    peak = df.groupby(['building', df['timestamp'].dt.date])['kwh'].max().reset_index()
    axes[2].scatter(peak["timestamp"], peak["kwh"])
    axes[2].set_title("Daily Peak Load")

    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
