import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard Olist",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard E-commerce Olist")

try:

    df = pd.read_csv("data/processed/orders_clean.csv")

    st.sidebar.header("Filtros")

    estados = st.sidebar.multiselect(
        "Estados",
        options=sorted(df["customer_state"].dropna().unique()),
        default=sorted(df["customer_state"].dropna().unique())
    )

    categorias = st.sidebar.multiselect(
        "Categorias",
        options=sorted(
            df["product_category_name_english"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df["product_category_name_english"]
            .dropna()
            .unique()
        )
    )

    filtered_df = df[
        (df["customer_state"].isin(estados)) &
        (
            df["product_category_name_english"]
            .isin(categorias)
        )
    ]

    st.subheader("📌 Principais Métricas")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Pedidos",
            filtered_df["order_id"].nunique()
        )

    with col2:
        st.metric(
            "Vendas Totais",
            f'R$ {filtered_df["payment_value"].sum():,.2f}'
        )

    with col3:
        st.metric(
            "Ticket Médio",
            f'R$ {filtered_df["payment_value"].mean():,.2f}'
        )

    with col4:
        st.metric(
            "Entrega Média",
            f'{filtered_df["delivery_time"].mean():.1f} dias'
        )

    with col5:
        st.metric(
            "Nota Média",
            f'⭐ {filtered_df["review_score"].mean():.1f}'
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📍 Pedidos por Estado")

        orders_state = (
            filtered_df.groupby("customer_state")["order_id"]
            .nunique()
            .reset_index()
            .sort_values(by="order_id", ascending=False)
        )

        fig1, ax1 = plt.subplots(figsize=(8, 4))

        ax1.bar(
            orders_state["customer_state"],
            orders_state["order_id"]
        )

        plt.xticks(rotation=45)

        st.pyplot(fig1)

    with col2:

        st.subheader("😊 Avaliações dos Clientes")

        reviews = (
            filtered_df["review_score"]
            .value_counts()
            .reset_index()
        )

        reviews.columns = [
            "Nota",
            "Quantidade"
        ]

        fig2, ax2 = plt.subplots(figsize=(6, 6))

        ax2.pie(
            reviews["Quantidade"],
            labels=reviews["Nota"],
            autopct='%1.1f%%'
        )

        st.pyplot(fig2)

    st.divider()

    st.subheader("🛍️ Top Categorias")

    category_sales = (
        filtered_df.groupby(
            "product_category_name_english"
        )["payment_value"]
        .sum()
        .reset_index()
        .sort_values(
            by="payment_value",
            ascending=False
        )
        .head(10)
    )

    fig3, ax3 = plt.subplots(figsize=(10, 5))

    ax3.barh(
        category_sales["product_category_name_english"],
        category_sales["payment_value"]
    )

    st.pyplot(fig3)

    st.divider()

    st.subheader("📈 Vendas ao Longo do Tempo")

    sales_time = (
        filtered_df.groupby("month_year")
        ["payment_value"]
        .sum()
        .reset_index()
    )

    fig4, ax4 = plt.subplots(figsize=(12, 5))

    ax4.plot(
        sales_time["month_year"],
        sales_time["payment_value"]
    )

    plt.xticks(rotation=45)

    st.pyplot(fig4)

    st.divider()

    st.subheader("📄 Dados")

    st.dataframe(filtered_df.head(100))

except Exception as e:

    st.error(f"Erro ao carregar dados: {e}")