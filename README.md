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
git clone <repository_url>
cd <repository_folder>
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
streamlit run app.py
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

---

## Deployment
Hasil Deployment Streamlit dapat dibuka melalui link berikut 
1. Upload proyek ke **GitHub** atau **GitLab**
2. Masuk ke [Streamlit Cloud](https://share.streamlit.io/)
3. Hubungkan repository Anda, pilih `app.py`, lalu deploy!

---
