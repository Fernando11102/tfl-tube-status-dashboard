import streamlit as st
import pandas as pd

st.title("London Underground Analytics Dashboard")

st.write("Transport service status analysis using Tfl data")

df = pd.read_csv("tube_status.csv")

df = df.dropna(subset=["status"])
df = df[df["status"] != "Unknown"]

disruptions = df[df["status"] != "Good Service"]

col1, col2, col3 = st.columns(3)

col1.metric("Total Lines", df["line"].nunique())
col2.metric("Good Service", (df["status"] == "Good Service").sum())
col3.metric("Disruptions", len(disruptions))

st.subheader("Service Status Distribution")

status_counts = df["status"].value_counts()
st.bar_chart(status_counts)

st.subheader("Underground Disruptions")
st.dataframe(disruptions[["line", "status"]])

st.subheader("Full Transport Dataset")
st.dataframe(df)