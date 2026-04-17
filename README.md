# MealSense: Mid-Day Meal Intelligence System

## Overview
This project analyzes and optimizes mid-day meal distribution in schools using data-driven techniques. It identifies inefficiencies, detects anomalies, and proposes an improved allocation strategy.

## Features
- Exploratory Data Analysis (EDA)
- Anomaly Detection (shortage, over-supply, quality issues)
- Correlation Analysis (food quality vs complaints)
- Rule-based Optimization (attendance + 5% buffer)

## Key Insights
- ~65% of days showed under-supply of meals
- High-attendance schools faced larger shortages
- Food quality strongly impacted complaints (r ≈ -0.46)
- Under-supply was the primary inefficiency (not over-supply)

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib / Seaborn

## How to Run
1. Open the notebook in Jupyter
2. Run all cells sequentially

## Future Improvements
- Real-time dashboard using Streamlit
- Integration with live attendance data
