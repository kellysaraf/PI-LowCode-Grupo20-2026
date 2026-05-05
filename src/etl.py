import pandas as pd
import os

def extract():
    print("Extraindo dados...")
    df = pd.read_csv("data/raw/olist_orders_dataset.csv")
    return df

def transform(df):
    print("Transformando dados...")
    df = df.dropna()
    return df

def load(df):
    print("Salvando dados tratados...")
    os.makedirs('data/processed', exist_ok=True) 
    df.to_csv('data/processed/orders_clean.csv', index=False)

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)