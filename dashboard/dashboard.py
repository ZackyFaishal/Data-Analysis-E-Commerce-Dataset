import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Atur layout agar lebih besar
st.set_page_config(layout="wide")

# Sidebar dengan foto profil
st.sidebar.header("Dashboard Analisis Data E-Commerce")
st.sidebar.image("./data/profile.png")
# Load dataset
@st.cache_data
def load_data():
    orders = pd.read_csv("./data/orders_dataset.csv")
    order_items = pd.read_csv("./data/order_items_dataset.csv")
    products = pd.read_csv("./data/products_dataset.csv")
    customers = pd.read_csv("./data/customers_dataset.csv")
    geolocation = pd.read_csv("./data/geolocation_dataset.csv")
    
    # Merge datasets untuk analisis
    df = pd.merge(order_items, orders, on="order_id", how="inner")
    df = pd.merge(df, products, on="product_id", how="inner")
    df = pd.merge(df, customers, on="customer_id", how="inner")
    return df

df = load_data()

# Pastikan kolom order_purchase_timestamp dikonversi ke datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Dapatkan rentang waktu dari dataset
min_date = df['order_purchase_timestamp'].min().date()
max_date = df['order_purchase_timestamp'].max().date()

# Filter interaktif berdasarkan rentang bulan
st.sidebar.subheader("Filter Data")
start_date = st.sidebar.date_input("Tanggal Mulai", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("Tanggal Akhir", max_date, min_value=min_date, max_value=max_date)

# Konversi date input ke datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

df_filtered = df[(df['order_purchase_timestamp'] >= start_date) & (df['order_purchase_timestamp'] <= end_date)]

option = st.sidebar.selectbox("Pilih Analisis:", [
    "Pola Jumlah Pesanan per Bulan", 
    "Kategori Produk Terlaris", 
    "Segmentasi Pelanggan (RFM Analysis)", 
    "Distribusi Geografis Pelanggan"
])

# Pola Jumlah Pesanan per Bulan
if option == "Pola Jumlah Pesanan per Bulan":
    st.subheader("Pola Jumlah Pesanan per Bulan")
    df_filtered['month'] = df_filtered['order_purchase_timestamp'].dt.to_period('M')
    monthly_orders = df_filtered.groupby('month')['order_id'].count()
    
    plt.figure(figsize=(15, 7))
    monthly_orders.plot(kind='line', marker='o', color='b')
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Pesanan")
    plt.title("Tren Jumlah Pesanan per Bulan")
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Kategori Produk Terlaris
elif option == "Kategori Produk Terlaris":
    st.subheader("Kategori Produk Terlaris")
    top_categories = df_filtered['product_category_name'].value_counts().nlargest(10)
    
    plt.figure(figsize=(15, 7))
    sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
    plt.xlabel("Jumlah Terjual")
    plt.ylabel("Kategori Produk")
    plt.title("10 Kategori Produk Terlaris")
    st.pyplot(plt)

elif option == "Segmentasi Pelanggan (RFM Analysis)":
    st.subheader("Segmentasi Pelanggan (RFM Analysis)")
    latest_date = df_filtered['order_purchase_timestamp'].max()
    
    # Hitung RFM
    rfm = df_filtered.groupby('customer_unique_id').agg({
        'order_purchase_timestamp': lambda x: (latest_date - x.max()).days,
        'order_id': 'count',
        'price': 'sum'
    }).rename(columns={
        'order_purchase_timestamp': 'Recency',
        'order_id': 'Frequency',
        'price': 'Monetary'
    })
    
    # Fungsi untuk mendeteksi outlier menggunakan IQR
    def remove_outliers(df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    # Bersihkan outlier dari setiap kolom RFM
    rfm_clean = remove_outliers(rfm, 'Recency')
    rfm_clean = remove_outliers(rfm_clean, 'Frequency')
    rfm_clean = remove_outliers(rfm_clean, 'Monetary')
    
    # Buat figure dengan 3 subplot
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    sns.histplot(rfm_clean['Recency'], bins=30, kde=True, ax=axes[0], color='blue')
    axes[0].set_title("Distribusi Recency")

    sns.histplot(rfm_clean['Frequency'], bins=30, kde=True, ax=axes[1], color='green')
    axes[1].set_title("Distribusi Frequency")

    sns.histplot(rfm_clean['Monetary'], bins=30, kde=True, ax=axes[2], color='red')
    axes[2].set_title("Distribusi Monetary")
    
    st.pyplot(fig)


    
# Distribusi Geografis Pelanggan
elif option == "Distribusi Geografis Pelanggan":
    st.subheader("Distribusi Geografis Pelanggan")
    city_counts = df_filtered['customer_city'].value_counts().nlargest(10)
    
    plt.figure(figsize=(15, 7))
    sns.barplot(x=city_counts.values, y=city_counts.index, palette='magma')
    plt.xlabel("Jumlah Pelanggan")
    plt.ylabel("Kota")
    plt.title("10 Kota dengan Pelanggan Terbanyak")
    st.pyplot(plt)

st.sidebar.write("Sumber data: Dataset E-Commerce")
