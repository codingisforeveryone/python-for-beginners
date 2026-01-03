# Web App with streamlit

## 🔗 API we’ll use: AlAdhan Prayer Times API

- Free
- No API key required

Example endpoint:

https://api.aladhan.com/v1/timingsByCity


## 📦 Install
```
pip install streamlit requests pandas
```

## 🧑‍💻 Streamlit Prayer Times App (Code)
```
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
```
▶️ Run the app
```
streamlit run app.py
```

Your browser opens with a Prayer Times dashboard 🌐

## Deploy App on streamlit

1. Create github account: https://github.com/
1. Create a public repository in that account: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
1. Add app.py file to that repository: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
1. Create streamlit account: https://share.streamlit.io/?utm_source=streamlit&utm_medium=referral&utm_campaign=main&utm_content=-ss-streamlit-io-topright
1. Connect streamlit account with your github repository (will be asked when you deploy the app)
1. Deploy the app

