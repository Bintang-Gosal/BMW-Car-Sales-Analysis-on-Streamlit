import streamlit as st
import pandas as pd
import line as f1
import pie as f2

st.set_page_config(layout="wide", page_title="Dashboard BMW Car Analysis (2010-2024)")
st.title("Main Dashboard for BMW Car Sales")
st.markdown("Welcome! Use the right menu to see the sales detail based on year and model.")

df = pd.read_csv("BMW_SALES.csv")
st.success(f"File {f1.file_csv} Success to read.")

st.subheader("Raw Data (First 10 Row)")
st.dataframe(df.head(10))

# --- Menampilkan Metrik Kunci ---
st.markdown("---")
st.subheader("Key Performance Index (KPI)")
kolom1, kolom2, kolom3 = st.columns(3)

# Menghitung dan menampilkan total penjualan
total_penjualan = df['Sales_Volume'].sum()
kolom1.metric("Total Sales", f"{total_penjualan:,} unit")

# Menghitung dan menampilkan rata-rata harga
rata_rata_harga = df['Price_USD'].mean()
kolom2.metric("Average Sales", f"${rata_rata_harga:,.2f}")

# Menghitung dan menampilkan jumlah model unik
jumlah_model = df['Model'].nunique()
kolom3.metric("Amount of Car Model", f"{jumlah_model:,}")