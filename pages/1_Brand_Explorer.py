import streamlit as st
import pandas as pd

st.title("🔍 Brand Explorer")

df = pd.read_csv("data/ethical_brands.csv")
category = st.selectbox("Filter by Category", sorted(df["category"].unique()))
min_labor = st.slider("Minimum Labor Rating", 1, 5, 3)

filtered = df[(df["category"] == category) & (df["labor_rating"] >= min_labor)]
st.write("### Filtered Brands")
st.dataframe(filtered)

selected_brand = st.selectbox("Choose a brand to view summary", filtered["brand"])
summary = filtered[filtered["brand"] == selected_brand]["summary"].values[0]
st.markdown(f"**Summary**: {summary}")
