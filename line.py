import pandas as pd
import plotly.express as px

file_csv = "BMW_SALES.csv"
df = pd.read_csv(file_csv)

df_copy = df.copy()
df_copy = df_copy.set_index("Year")
revenue = df_copy.groupby(df_copy.index)["Sales_Volume"].sum().reset_index()

def create_line_chart(df):
    df_copy["Order_Year"] = df_copy.index
    revenue = df_copy.groupby("Year")["Sales_Volume"].sum().reset_index()
    revenue.columns = ['Year', 'Sales_Volume']

    fig = px.line(
        data_frame= revenue,
        x="Year",
        y='Sales_Volume',
        title='Company Revenue'
        )
    return fig