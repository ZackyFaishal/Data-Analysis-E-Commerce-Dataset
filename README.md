# Dashboard Analisis Data E-Commerce

## Deskripsi Proyek
Proyek ini adalah sebuah dashboard interaktif berbasis **Streamlit** untuk menampilkan hasil analisis data e-commerce, termasuk:
- Pola jumlah pesanan per bulan
- Kategori produk terlaris
- Segmentasi pelanggan berdasarkan **RFM Analysis**
- Distribusi geografis pelanggan

Dashboard ini membantu dalam memahami pola transaksi, preferensi pelanggan, serta memberikan wawasan yang lebih mendalam terhadap bisnis e-commerce berdasarkan dataset yang digunakan.

---

## Instalasi
### 1. Clone Repository
Jika proyek ini di-host di GitHub, Anda dapat meng-clone-nya dengan perintah berikut:
```bash
git clone https://github.com/ZackyFaishal/Data-Analysis-E-Commerce-Dataset.git
```

### 2. Buat Virtual Environment (Opsional)
Sebaiknya gunakan virtual environment untuk menghindari konflik dependensi.
```bash
python -m venv env
source env/bin/activate   # Untuk Mac/Linux
env\Scripts\activate      # Untuk Windows
```

### 3. Install Dependensi
Jalankan perintah berikut untuk menginstal paket yang dibutuhkan:
```bash
pip install -r requirements.txt
```
Jika file `requirements.txt` belum tersedia, berikut beberapa library utama yang perlu diinstal:
```bash
pip install streamlit pandas matplotlib seaborn
```

---

## Menjalankan Dashboard
Setelah instalasi berhasil, jalankan dashboard dengan perintah berikut:
```bash
streamlit run dashboard/dashboard.py
```
Setelah dijalankan, Streamlit akan otomatis membuka browser pada `http://localhost:8501/`, dan Anda dapat mulai menggunakan dashboard.

---

## Struktur Proyek
Berikut adalah struktur direktori proyek ini:
```
.
├── data/                     # Folder untuk dataset CSV
│   ├── orders_dataset.csv
│   ├── order_items_dataset.csv
│   ├── products_dataset.csv
│   ├── customers_dataset.csv
│   ├── geolocation_dataset.csv
│   ├── ....
│
├── dashboard/                   # Folder untuk dashboard
│   ├── profile.jpg
|   ├── dashboard.py
│
├── notebook.py                # File notebook untuk data analyst
├── requirements.txt           # Daftar dependensi Python
├── README.md                  # Dokumentasi proyek ini
```

## Deployment
Saya telah melakukan deploy ke **Streamlit Cloud**, Klik link berikut untuk melihat hasilnya :
[data analysis zacky](https://zacky-data-analysis-e-commerce.streamlit.app)

Terima kasih
