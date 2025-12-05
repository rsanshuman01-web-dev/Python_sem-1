from ingestion import read_all_csvs
from aggregations import calculate_daily_totals, calculate_weekly_aggregates, building_wise_summary
from models import BuildingManager
from viz import create_dashboard
import os

def main():
    df, bad = read_all_csvs("data")

    if df.empty:
        print("No data found! Add CSV files in the data folder.")
        return

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/cleaned_energy_data.csv", index=False)

    daily = calculate_daily_totals(df)
    weekly = calculate_weekly_aggregates(df)
    summary = building_wise_summary(df)

    summary.to_csv("output/building_summary.csv", index=False)

    manager = BuildingManager()
    manager.add_from_dataframe(df)
    reports = manager.summary()

    peak_time = df.loc[df["kwh"].idxmax()]["timestamp"]
    total_campus = summary["total_kwh"].sum()
    top_building = summary.sort_values("total_kwh", ascending=False).iloc[0]

    with open("output/summary.txt", "w") as f:
        f.write(f"Total Campus Consumption: {total_campus}\n")
        f.write(f"Highest Consuming Building: {top_building['building']}\n")
        f.write(f"Peak Load Time: {peak_time}\n")

    create_dashboard(daily, weekly, df, out_path="output/dashboard.png")

    print("All files generated inside output/ folder.")

if __name__ == "__main__":
    main()
