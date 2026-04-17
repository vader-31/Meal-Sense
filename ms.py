import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="MealSense", layout="centered")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("midday_meal_cleaned.csv")

# ---------------- TITLE ----------------
st.title("🍽️ MealSense: Mid-Day Meal Intelligence System")

st.write("Analyze and optimize school meal distribution using data-driven insights")

# ---------------- INPUT ----------------
st.subheader("📥 Input")

attendance = st.number_input("Enter Attendance", min_value=0, step=1)

# ---------------- LOGIC ----------------
if attendance > 0:
    recommended_meals = int(attendance * 1.05)

    st.subheader("📊 Meal Recommendation")

    st.metric("Recommended Meals", recommended_meals)

    gap = recommended_meals - attendance
    st.write(f"Extra buffer: {gap}")

    if attendance > 80:
        st.warning("⚠️ High demand school - monitor closely")
    else:
        st.success("✅ Normal demand")

# ---------------- SCHOOL ANALYSIS ----------------
st.subheader("🏫 School Insights")

school_id = st.selectbox("Select School ID", sorted(df["school_id"].unique()))

school_data = df[df["school_id"] == school_id]

avg_attendance = int(school_data["attendance"].mean())
avg_meals = int(school_data["meals_served"].mean())

st.write(f"Average Attendance: {avg_attendance}")
st.write(f"Average Meals Served: {avg_meals}")

if avg_meals < avg_attendance:
    st.error("⚠️ Under-supply risk detected")
else:
    st.success("✅ Supply sufficient")

# ---------------- VISUALIZATION ----------------
st.subheader("📈 Meals Distribution")

chart_data = df.groupby("school_id")["meals_served"].mean()

st.bar_chart(chart_data)

# ---------------- SYSTEM INSIGHTS ----------------
st.subheader("📌 System Insights")

shortage_days = (df["meals_served"] < df["attendance"]).sum()

st.write(f"Total shortage days in dataset: {shortage_days}")