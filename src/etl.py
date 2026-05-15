import pandas as pd

def extract():

    orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

    order_items = pd.read_csv(
        "data/raw/olist_order_items_dataset.csv"
    )

    payments = pd.read_csv(
        "data/raw/olist_order_payments_dataset.csv"
    )

    reviews = pd.read_csv(
        "data/raw/olist_order_reviews_dataset.csv"
    )

    customers = pd.read_csv(
        "data/raw/olist_customers_dataset.csv"
    )

    products = pd.read_csv(
        "data/raw/olist_products_dataset.csv"
    )

    translation = pd.read_csv(
        "data/raw/product_category_name_translation.csv"
    )

    return (
        orders,
        order_items,
        payments,
        reviews,
        customers,
        products,
        translation
    )

def transform(
    orders,
    order_items,
    payments,
    reviews,
    customers,
    products,
    translation
):

    orders["order_purchase_timestamp"] = pd.to_datetime(
        orders["order_purchase_timestamp"]
    )

    orders["order_delivered_customer_date"] = pd.to_datetime(
        orders["order_delivered_customer_date"]
    )

    orders["delivery_time"] = (
        orders["order_delivered_customer_date"]
        - orders["order_purchase_timestamp"]
    ).dt.days

    orders["month_year"] = (
        orders["order_purchase_timestamp"]
        .dt.to_period("M")
        .astype(str)
    )

    products = products.merge(
        translation,
        on="product_category_name",
        how="left"
    )

    df = orders.merge(
        customers,
        on="customer_id",
        how="left"
    )

    df = df.merge(
        order_items,
        on="order_id",
        how="left"
    )

    df = df.merge(
        payments,
        on="order_id",
        how="left"
    )

    df = df.merge(
        reviews,
        on="order_id",
        how="left"
    )

    df = df.merge(
        products,
        on="product_id",
        how="left"
    )

    df = df.drop_duplicates()

    df["review_score"] = df["review_score"].fillna(0)

    df["delivery_time"] = df["delivery_time"].fillna(0)

    return df

def load(df):

    df.to_csv(
        "data/processed/orders_clean.csv",
        index=False
    )

if __name__ == "__main__":

    (
        orders,
        order_items,
        payments,
        reviews,
        customers,
        products,
        translation
    ) = extract()

    df = transform(
        orders,
        order_items,
        payments,
        reviews,
        customers,
        products,
        translation
    )

    load(df)

    print("ETL finalizado com sucesso!")