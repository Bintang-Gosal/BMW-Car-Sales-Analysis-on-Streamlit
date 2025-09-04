import streamlit as st
import pandas as pd
import line as f1

# Membaca data
df = pd.read_csv("BMW_SALES.csv")

df["Year"] = df["Year"].astype(int)

min_year = int(df["Year"].min())
max_year = int(df["Year"].max())

selected_years = st.sidebar.slider(
    "Choose a year",
    min_value= min_year,
    max_value= max_year,
    value=(min_year, max_year)
    )

st.title(f"BMW Car Sales - Yearly Sales from {selected_years[0]} - {selected_years[1]}")

# --- Terapkan Filter ---
# Filter data berdasarkan rentang tahun yang dipilih
df_filtered = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]
df_filtered = df_filtered.groupby("Year")["Sales_Volume"].sum()

# --- Menampilkan Grafik ---
df_to_plot = df_filtered.reset_index()
line_chart_fig = f1.create_line_chart(df_to_plot)
st.plotly_chart(line_chart_fig, use_container_width=True)

# --- Menampilkan Dataframe yang Sudah Difilter ---
st.subheader("Filtered Data")
st.dataframe(df_filtered.to_frame().style.format('{:,}'))