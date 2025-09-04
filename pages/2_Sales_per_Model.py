import streamlit as st
import pandas as pd
import pie as f2

# Membaca data
df = pd.read_csv("BMW_SALES.csv")

df["Year"] = df["Year"].astype(int)

min_year = int(df["Year"].min())
max_year = int(df["Year"].max())

selected_years = st.sidebar.slider(
    "Choose a year",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

st.title(f"BMW Car Sales - Sales Per Model {selected_years[0]} - {selected_years[1]}")

df_filtered = df[(df["Year"] >= selected_years[0]) & (df["Year"] <= selected_years[1])]
df_final = df_filtered.groupby("Model")["Sales_Volume"].sum()

# Tampilkan grafik
pie_chart_fig = f2.create_pie_chart(df_filtered)
st.plotly_chart(pie_chart_fig, use_container_width=True)

# dataframe filter
st.subheader("Filtered Data")
st.dataframe(df_final.to_frame().style.format('{:,}'))