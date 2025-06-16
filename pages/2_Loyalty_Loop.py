import streamlit as st
import pandas as pd

st.title("🎁 LoyaltyLoop")

user_df = pd.read_csv("data/user_profiles.csv")
brand_df = pd.read_csv("data/ethical_brands.csv")

user = st.selectbox("Select User", user_df["name"].tolist())
user_data = user_df[user_df["name"] == user].iloc[0]

st.markdown(f"**Hello {user}!**")
st.write(f"- Eco-conscious: {user_data['eco_conscious']}")
st.write(f"- Points: {user_data['points']}")
st.write(f"- Consent Level: {user_data['consent_level']}")

# Recommend ethical brands
recommend = brand_df[
    (brand_df["labor_rating"] >= 4) & 
    (brand_df["carbon_rating"] >= 4)
]
st.write("### Recommended Brands For You")
st.dataframe(recommend[["brand", "category", "labor_rating", "carbon_rating"]])

# Simulate earning points
if st.button("Simulate Ethical Action (+10 pts)"):
    user_df.loc[user_df["name"] == user, "points"] += 10
    user_df.to_csv("data/user_profiles.csv", index=False)
    st.success("Points added!")
