import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_parquet("data/green_tripdata_2024-12.parquet")
print(df.shape)
print(df.head())

# convert pickup and dropoff to datetime
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

#  trip duration in minutes
df['trip_duration'] = (df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime']).dt.total_seconds() / 60

print(df[['lpep_pickup_datetime', 'lpep_dropoff_datetime', 'trip_duration']].head())

df = df[(df['trip_duration'] > 0) & (df['trip_duration'] <= 120)]
df = df[df['trip_distance'] > 0]

print(df[['trip_duration', 'trip_distance', 'total_amount']].describe())

# visuals to mainly help us determine price clusters
plt.figure(figsize=(10, 5))
sns.histplot(df['trip_duration'], bins=50, kde=True)
plt.title("Distribution of Trip Duration (minutes)")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='trip_distance', y='total_amount', alpha=0.3)
plt.title("Trip Distance vs Total Amount")
plt.xlabel("Trip Distance (miles)")
plt.ylabel("Total Fare ($)")
plt.xlim(0, 20)   # adjust based on your data
plt.ylim(0, 100)  # same here
plt.show()

# avg fare by hour of day to help determine peak/rush hours
df['pickup_hour'] = df['lpep_pickup_datetime'].dt.hour
avg_fare_by_hour = df.groupby('pickup_hour')['total_amount'].mean()

plt.figure(figsize=(10, 5))
avg_fare_by_hour.plot(kind='bar')
plt.title("Average Fare by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Average Fare ($)")
plt.xticks(rotation=0)
plt.show()

zones = pd.read_csv("data/taxi_zone_lookup.csv")
df = df.merge(zones, how='left', left_on='PULocationID', right_on='LocationID')

# now to look and plot for the most popular pickup zones
top_zones = df['Zone'].value_counts().head(10)
print(top_zones)

top_zones.plot(kind='barh', title='Top 10 Pickup Zones (Dec 2024)')
plt.xlabel("Number of Trips")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
