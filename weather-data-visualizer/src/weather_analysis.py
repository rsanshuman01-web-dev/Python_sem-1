import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Make sure output folder exists
os.makedirs("../output", exist_ok=True)

# ---------------------------
# TASK 1: LOAD DATA
# ---------------------------

df = pd.read_csv("../data/DailyDelhiClimateTrain.csv")

print("Initial Data:")
print(df.head())
print(df.info())
print(df.describe())

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# ---------------------------
# TASK 2: CLEANING
# ---------------------------

df = df.dropna()
df.rename(columns={
    "meantemp": "temperature",
    "humidity": "humidity",
    "wind_speed": "wind_speed",
    "meanpressure": "pressure"
}, inplace=True)

df.to_csv("../output/cleaned_weather_data.csv", index=False)

# ---------------------------
# TASK 3: STATISTICS
# ---------------------------

daily_mean = np.mean(df['temperature'])
daily_max = np.max(df['temperature'])
daily_min = np.min(df['temperature'])
daily_std = np.std(df['temperature'])

print("\nDaily Temperature Stats:")
print("Mean:", daily_mean)
print("Max:", daily_max)
print("Min:", daily_min)
print("Std Dev:", daily_std)

df['month'] = df['date'].dt.month
monthly_stats = df.groupby('month')['temperature'].agg(['mean', 'min', 'max', 'std'])

print("\nMonthly Temperature Stats:")
print(monthly_stats)

# ---------------------------
# VISUALIZATION
# ---------------------------

# Line chart
plt.figure(figsize=(10,4))
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("../output/daily_temperature_trend.png")
plt.close()

# Bar chart (monthly averages)
monthly_avg = df.groupby('month')['temperature'].mean()
plt.figure(figsize=(10,4))
plt.bar(monthly_avg.index, monthly_avg.values)
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.savefig("../output/monthly_rainfall_bar_chart.png")
plt.close()

# Scatter
plt.figure(figsize=(6,4))
plt.scatter(df['humidity'], df['temperature'])
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature")
plt.savefig("../output/humidity_vs_temperature_scatter.png")
plt.close()

# Combined plot
fig, axs = plt.subplots(1, 2, figsize=(12,4))

axs[0].plot(df['date'], df['temperature'])
axs[0].set_title("Temperature Trend")

axs[1].scatter(df['humidity'], df['temperature'])
axs[1].set_title("Humidity vs Temperature")

plt.tight_layout()
plt.savefig("../output/combined_plots.png")
plt.close()

print("All plots and cleaned data saved successfully!")

