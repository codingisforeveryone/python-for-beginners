import requests
import streamlit as st
import pandas as pd

st.title("🕌 Prayer Times App")

city = st.text_input("Enter City", "Makkah")
country = st.text_input("Enter Country", "Saudi Arabia")

if st.button("Get Prayer Times"):
    url = "https://api.aladhan.com/v1/timingsByCity"
    params = {
        "city": city,
        "country": country,
        "method": 4  # Umm Al-Qura method
    }

    response = requests.get(url, params=params).json()
    timings = response["data"]["timings"]

    prayer_times = {
        "Fajr": timings["Fajr"],
        "Dhuhr": timings["Dhuhr"],
        "Asr": timings["Asr"],
        "Maghrib": timings["Maghrib"],
        "Isha": timings["Isha"]
    }

    df = pd.DataFrame(prayer_times.items(), columns=["Prayer", "Time"])

    st.subheader(f"📍 Prayer Times in {city}")
    st.table(df)