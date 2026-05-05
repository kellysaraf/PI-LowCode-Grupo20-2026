import streamlit as st
import pandas as pd

st.title("Dashboard - E-commerce Olist")

try:
    df = pd.read_csv("data/processed/orders_clean.csv")

    st.metric("Total de pedidos", len(df))

    st.write("Dados:")
    st.dataframe(df.head())

except:
    st.warning("Execute o ETL antes para gerar os dados.")
