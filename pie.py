import pandas as pd
import plotly.express as px

file_csv = "BMW_SALES.csv"
df = pd.read_csv(file_csv)

df_copy = df.copy()
revenue = df_copy.groupby("Model")["Sales_Volume"].sum().reset_index()

def create_pie_chart(df):
    revenue 

    fig = px.pie(
        data_frame= revenue,
        values="Sales_Volume",
        names='Model',
        title='Pie Chart About Bestseller Car'
        )
    return fig