import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("🧠 AI Sentiment & Summarizer")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    res = requests.post(
        f"{API_URL}/token",
        data={"username": username, "password": password}
    )
    if res.status_code == 200:
        st.session_state.token = res.json()["access_token"]
        st.success("Logged in!")
    else:
        st.error("Login failed")

if "token" in st.session_state:
    text = st.text_area("Enter text")

    if st.button("Analyze Sentiment"):
        res = requests.post(
            f"{API_URL}/sentiment",
            params={"text": text},
            headers={"Authorization": f"Bearer {st.session_state.token}"}
        )
        st.json(res.json())

    if st.button("Summarize"):
        res = requests.post(
            f"{API_URL}/summarize",
            params={"text": text},
            headers={"Authorization": f"Bearer {st.session_state.token}"}
        )
        st.success(res.json()["summary"])
