import streamlit as st

def visualize_ayah_and_translation(ayah, translation):
    st.set_page_config(layout="wide")

    st.markdown(
        """
        <style>
        .arabic {
            direction: rtl;
            text-align: right;
            font-size: 40px;   /* 🔥 increase size here */
            line-height: 2.4;
            font-family: "Amiri", "Scheherazade", serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        f"<div class='arabic'>{ayah}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='arabic'>{translation}</div>",
        unsafe_allow_html=True
    )
