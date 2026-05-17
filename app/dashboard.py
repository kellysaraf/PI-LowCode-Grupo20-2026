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
    # Carregando os dados
    df = pd.read_csv("data/processed/orders_clean.csv")

    st.sidebar.header("Filtros")

    # Filtro de Estados
    estados = st.sidebar.multiselect(
        "Estados",
        options=sorted(df["customer_state"].dropna().unique()),
        default=sorted(df["customer_state"].dropna().unique())
    )

    # Filtro de Categorias
    categorias = st.sidebar.multiselect(
        "Categorias",
        options=sorted(df["product_category_name_english"].dropna().unique()),
        default=sorted(df["product_category_name_english"].dropna().unique())
    )

    # NOVO: Filtro de Período (Mês/Ano)
    if "month_year" in df.columns:
        meses = st.sidebar.multiselect(
            "Período (Mês/Ano)",
            options=sorted(df["month_year"].dropna().unique()),
            default=sorted(df["month_year"].dropna().unique())
        )
    else:
        meses = []

    # Aplicando os filtros no Dataframe
    if "month_year" in df.columns:
        filtered_df = df[
            (df["customer_state"].isin(estados)) &
            (df["product_category_name_english"].isin(categorias)) &
            (df["month_year"].isin(meses))
        ]
    else:
        filtered_df = df[
            (df["customer_state"].isin(estados)) &
            (df["product_category_name_english"].isin(categorias))
        ]

    st.subheader("📌 Principais Métricas")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Pedidos", filtered_df["order_id"].nunique())

    with col2:
        st.metric("Vendas Totais", f'R$ {filtered_df["payment_value"].sum():,.2f}')

    with col3:
        st.metric("Ticket Médio", f'R$ {filtered_df["payment_value"].mean():,.2f}')

    with col4:
        st.metric("Entrega Média", f'{filtered_df["delivery_time"].mean():.1f} dias')

    with col5:
        st.metric("Nota Média", f'⭐ {filtered_df["review_score"].mean():.1f}')

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📍 Pedidos por Estado")
        orders_state = (
            filtered_df.groupby("customer_state")["order_id"]
            .nunique()
            .reset_index()
        )
        st.bar_chart(data=orders_state.set_index("customer_state"))

    with col2:
        st.subheader("😊 Avaliações dos Clientes")
        reviews = filtered_df["review_score"].value_counts().reset_index()
        reviews.columns = ["Nota", "Quantidade"]
        
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        ax2.pie(
            reviews["Quantidade"],
            labels=reviews["Nota"],
            autopct='%1.1f%%'
        )
        st.pyplot(fig2)

    st.divider()

    st.subheader("🚚 Tempo Médio de Entrega por Estado")
    delivery_state = (
        filtered_df.groupby("customer_state")["delivery_time"]
        .mean()
        .reset_index()
    )
    st.bar_chart(data=delivery_state.set_index("customer_state"))

    st.divider()

    st.subheader("🛍️ Top Categorias (Faturamento)")
    category_sales = (
        filtered_df.groupby("product_category_name_english")["payment_value"]
        .sum()
        .reset_index()
        .sort_values(by="payment_value", ascending=False)
        .head(10)
    )
    st.bar_chart(data=category_sales.set_index("product_category_name_english"))

    st.divider()

    st.subheader("📈 Vendas ao Longo do Tempo")
    if "month_year" in filtered_df.columns:
        sales_time = (
            filtered_df.groupby("month_year")["payment_value"]
            .sum()
            .reset_index()
        )
        st.line_chart(data=sales_time.set_index("month_year"))
    else:
        st.warning("Coluna 'month_year' não encontrada na base de dados para gerar este gráfico.")

    st.divider()

    st.subheader("📄 Dados")
    st.dataframe(filtered_df.head(100))

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}. Verifique se o caminho do arquivo 'orders_clean.csv' está correto no repositório.")
