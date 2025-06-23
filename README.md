#NYC Green Taxi Trip Analysis (December 2024)#

This project analyzes the NYC Green Taxi dataset for December 2024 using Python. It explores trends in taxi activity by location, time, and volume to extract actionable insights on urban mobility patterns.

## 📊 Key Objectives

- Clean and prepare the Green Taxi trip data
- Merge with NYC Taxi Zone Lookup data
- Analyze pickup and drop-off locations
- Visualize traffic intensity by zone and time
- Identify trends during holiday season and peak hours

## 📁 Project Structure
NYCgreentaxi/
├── nycGreentaxianalysis.py # Main analysis script
├── green_tripdata_2024-12.parquet # Input trip data
├── taxi_zone_lookup.csv # Zone metadata
├── visual_insights/ # Output charts and graphs
│ ├── top_pickup_zones.png
│ ├── traffic_by_month.png
│ └── ... (more visual files)
└── README.md

## 📷 Visual Insights

### Top Pickup Zones
![Top Pickup Zones](visual_insights/top_pickup_zones.png)

### Monthly Traffic Patterns
![Monthly Traffic](visual_insights/traffic_by_month.png)

> More charts are available in the `visual_insights/` folder.

## Tools & Libraries

- Python 3.11
- Pandas
- Matplotlib
- Seaborn

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/sy549/NYCgreentaxi.git
   cd NYCgreentaxi
2. Download dependencies
   pip install -r requirements.txt

3. Run
4. python nycGreentaxianalysis.py



