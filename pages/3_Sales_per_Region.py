import streamlit as st
import pandas as pd
import pie2 as f3

st.title("BMW Car Sales - Penjualan Per Daerah")

# Membaca data
df = pd.read_csv("BMW_SALES.csv")

df["Year"] = df["Year"].astype(int)

# --- Filter Interaktif di Sidebar ---
min_year = int(df["Year"].min())
max_year = int(df["Year"].max())

selected_years = st.sidebar.slider(
    "Choose a Year",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

all_region = df["Region"].unique()
list_region = ["Semua Area"] + list(all_region)

selected_region = st.sidebar.selectbox(
    "Pilih Wilayah",
    list_region
)

# --- Logika Pemfilteran ---
# 1. Terapkan filter TAHUN pada DataFrame awal.
df_filtered = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]

# 2. Terapkan filter WILAYAH HANYA JIKA pengguna tidak memilih "Semua Area".
if selected_region != "Semua Area":
    df_filtered = df_filtered[df_filtered["Region"] == selected_region]

# --- Menampilkan Grafik dan Dataframe yang Sudah Difilter ---
st.subheader(f"Sales Per Region ({selected_years[0]} - {selected_years[1]})")

# Logika Tampilan Adaptif
if selected_region == "Semua Area":
    # Agregasi data yang sudah difilter untuk pie chart
    df_final = df_filtered.groupby("Region")["Sales_Volume"].sum().reset_index()

    pie_chart = f3.create_pie_chart(df_final)
    st.plotly_chart(pie_chart, use_container_width=True)

    st.subheader("Filtered Data")
    st.dataframe(df_final.style.format({'Sales_Volume': '{:,}'}))

else:
    # Jika satu wilayah dipilih, tampilkan metrik total penjualan
    total_sales = df_filtered["Sales_Volume"].sum()
    st.metric(label=f"Total Sales on {selected_region}", value=f"{total_sales:,}")