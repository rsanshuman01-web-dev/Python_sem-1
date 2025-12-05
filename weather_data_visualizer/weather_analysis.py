# weather_analysis.py
"""
Weather Data Visualizer
Assignment script for Programming for Problem Solving using Python
Author: Anshuman Sharma
Dataset file expected: data/DailyDelhiClimateTrain.csv
Outputs:
 - cleaned_data.csv
 - plots: daily_temp_line.png, monthly_rainfall_bar.png,
          humidity_vs_temp_scatter.png, combined_plots.png
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Config ----------
DATA_PATH = "DailyDelhiClimateTrain.csv"   # make sure this filename matches your uploaded CSV
OUTPUT_DIR = "."
CLEANED_CSV = os.path.join(OUTPUT_DIR, "cleaned_data.csv")
PLOT_DAILY_TEMP = os.path.join(OUTPUT_DIR, "daily_temp_line.png")
PLOT_MONTHLY_RAIN = os.path.join(OUTPUT_DIR, "monthly_rainfall_bar.png")
PLOT_SCATTER = os.path.join(OUTPUT_DIR, "humidity_vs_temp_scatter.png")
PLOT_COMBINED = os.path.join(OUTPUT_DIR, "combined_plots.png")

# ---------- Helper functions ----------
def safe_read_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV file not found at: {path}")
    df = pd.read_csv(path)
    return df

def ensure_datetime(df):
    # try to find a date-like column
    date_cols = [c for c in df.columns if "date" in c.lower()]
    if not date_cols:
        raise ValueError("No date column found. Make sure your CSV has a 'date' column.")
    col = date_cols[0]
    df[col] = pd.to_datetime(df[col], errors="coerce")
    df = df.rename(columns={col: "date"})
    return df

def choose_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None

# ---------- Load data ----------
print("Loading data...")
df = safe_read_csv(DATA_PATH)
print("Columns found:", list(df.columns))

# ---------- Prepare data ----------
df = ensure_datetime(df)
df = df.sort_values("date").reset_index(drop=True)

# Identify commonly-used columns (names differ across datasets)
temp_col = choose_column(df, ["meantemp", "temp", "temperature", "mean_temp"])
humidity_col = choose_column(df, ["humidity", "hum"])
rain_col = choose_column(df, ["rainfall", "rain", "precipitation", "precip"])
wind_col = choose_column(df, ["wind_speed", "windspeed", "wind"])

print("Detected columns -> temp:", temp_col, "humidity:", humidity_col, "rain:", rain_col, "wind:", wind_col)

# ---------- Cleaning ----------
# 1. Convert numeric columns to numeric and handle missing data
numeric_cols = []
for c in [temp_col, humidity_col, rain_col, wind_col]:
    if c is not None:
        df[c] = pd.to_numeric(df[c], errors="coerce")
        numeric_cols.append(c)

# 2. Fill or drop NaNs: strategy = forward-fill then backward-fill, then drop remaining
df[numeric_cols] = df[numeric_cols].ffill().bfill()
df = df.dropna(subset=["date"])  # ensure dates exist

# Save cleaned CSV
df.to_csv(CLEANED_CSV, index=False)
print(f"Cleaned data saved to {CLEANED_CSV}")

# ---------- Statistical Analysis ----------
import datetime as dt

# daily stats (just show descriptive stats)
print("\nDaily statistics (head):")
print(df.head())

# Monthly / yearly stats via resample (requires date as index)
df_indexed = df.set_index("date")
monthly = df_indexed.resample("M")
yearly = df_indexed.resample("Y")

stats = {}
for name, group in [("daily", df_indexed), ("monthly", monthly), ("yearly", yearly)]:
    if name == "daily":
        # for daily, use describe on numeric columns
        stats[name] = df_indexed[numeric_cols].describe() if numeric_cols else None
    else:
        stats[name] = group[numeric_cols].agg([np.mean, np.min, np.max, np.std]) if numeric_cols else None

print("\nComputed statistics keys:", list(stats.keys()))

# ---------- Visualizations ----------
plt.rcParams.update({'figure.max_open_warning': 0})  # avoid warnings in some environments

# 1) Line chart for daily temperature trends (if temp exists)
if temp_col:
    plt.figure(figsize=(12,4))
    plt.plot(df_indexed.index, df_indexed[temp_col], linewidth=0.8)
    plt.title("Daily Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel(temp_col)
    plt.tight_layout()
    plt.savefig(PLOT_DAILY_TEMP)
    plt.close()
    print(f"Saved daily temperature plot: {PLOT_DAILY_TEMP}")
else:
    print("Temperature column not found — skipping daily temperature plot.")

# 2) Bar chart for monthly rainfall totals (if rain exists)
if rain_col:
    monthly_rain = df_indexed[rain_col].resample("M").sum()
    plt.figure(figsize=(10,4))
    monthly_rain.plot(kind="bar", width=0.8)
    plt.title("Monthly Rainfall Totals")
    plt.xlabel("Month")
    plt.ylabel(f"Total {rain_col}")
    plt.tight_layout()
    plt.savefig(PLOT_MONTHLY_RAIN)
    plt.close()
    print(f"Saved monthly rainfall plot: {PLOT_MONTHLY_RAIN}")
else:
    print("Rainfall column not found — skipping monthly rainfall bar chart.")

# 3) Scatter plot humidity vs temp
if temp_col and humidity_col:
    plt.figure(figsize=(6,5))
    plt.scatter(df_indexed[temp_col], df_indexed[humidity_col], alpha=0.5, s=10)
    plt.title("Humidity vs Temperature")
    plt.xlabel(temp_col)
    plt.ylabel(humidity_col)
    plt.tight_layout()
    plt.savefig(PLOT_SCATTER)
    plt.close()
    print(f"Saved humidity vs temperature scatter: {PLOT_SCATTER}")
else:
    print("Either temperature or humidity column missing — skipping scatter plot.")

# 4) Combined figure with two plots (example: temp line + humidity scatter)
fig, axes = plt.subplots(1,2, figsize=(14,4))
made_any = False

if temp_col:
    axes[0].plot(df_indexed.index, df_indexed[temp_col], linewidth=0.7)
    axes[0].set_title("Daily Temperature")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel(temp_col)
    made_any = True
else:
    axes[0].text(0.5, 0.5, "No temp column", ha="center", va="center")
    axes[0].set_title("Daily Temperature")

if temp_col and humidity_col:
    axes[1].scatter(df_indexed[temp_col], df_indexed[humidity_col], s=8, alpha=0.5)
    axes[1].set_title("Humidity vs Temperature")
    axes[1].set_xlabel(temp_col)
    axes[1].set_ylabel(humidity_col)
    made_any = True
else:
    axes[1].text(0.5, 0.5, "Insufficient cols", ha="center", va="center")
    axes[1].set_title("Humidity vs Temperature")

plt.tight_layout()
plt.savefig(PLOT_COMBINED)
plt.close()
print(f"Saved combined plot: {PLOT_COMBINED}")

# ---------- Summary outputs ----------
print("\n----- Summary -----")
print("Rows:", len(df))
print("Numeric columns used:", numeric_cols)
print("Saved plots (check repository root):")
for p in [PLOT_DAILY_TEMP, PLOT_MONTHLY_RAIN, PLOT_SCATTER, PLOT_COMBINED]:
    if os.path.exists(p):
        print(" -", p)
print("Script finished successfully.")

