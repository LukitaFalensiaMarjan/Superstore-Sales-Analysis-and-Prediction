# Proyek Analisis & Prediksi Penjualan Superstore

Proyek ini menganalisis data penjualan Superstore selama 4 tahun (2017-2020) untuk menemukan pendorong utama keuntungan (profit) dan membangun model machine learning untuk memprediksi profitabilitas di masa depan serta total penjualan.

## Struktur Folder Proyek

(Anda bisa salin-tempel struktur pohon dari `image_99e7c6.png` Anda di sini)

## Temuan Utama & Wawasan (dari EDA)

Setelah menganalisis data, berikut adalah 3 temuan paling penting:

1.  **Profitabilitas Sangat Bergantung pada Kategori & Diskon:**
    * Meskipun kategori **Technology** dan **Office Supplies** sangat menguntungkan, kategori **Furniture** secara keseluruhan nyaris tidak untung.
    * *Sub-kategori 'Tables' dan 'Bookcases' adalah biang kerok kerugian terbesar.* (Lihat: `reports/figures/2_profit_by_category.png`)

2.  **Diskon Adalah Pedang Bermata Dua:**
    * Ada korelasi negatif yang kuat antara Diskon dan Profit.
    * *Pemberian diskon di atas 30% hampir selalu (lebih dari 90% kasus) mengakibatkan kerugian.* (Lihat: `reports/figures/3_discount_vs_profit.png`)

3.  **Penjualan Memiliki Pola Musiman (Seasonal) yang Jelas:**
    * Penjualan selalu memuncak di akhir tahun (Q4), terutama di bulan November dan Desember, dan mencapai titik terendah di awal tahun (Q1), terutama Februari. (Lihat: `reports/figures/5_ts_monthly_sales.png`)

## Rekomendasi Bisnis

Berdasarkan temuan di atas, berikut adalah rekomendasi yang dapat ditindaklanjuti:

1.  **Segera Tinjau Ulang Strategi Diskon:**
    * **Tindakan:** Tetapkan batas maksimal diskon (disarankan 20-25%) untuk sub-kategori yang merugi seperti 'Tables'.
    * **Dampak:** Mengurangi kerugian secara signifikan tanpa harus menghentikan penjualan.

2.  **Optimalkan Manajemen Stok (Inventory):**
    * **Tindakan:** Tingkatkan stok barang-barang *best-seller* (seperti 'Copiers' dan 'Phones') menjelang Q4 (Oktober-Desember) untuk mengantisipasi lonjakan permintaan.
    * **Dampak:** Memaksimalkan pendapatan di musim puncak.

3.  **Luncurkan Kampanye Pemasaran di Musim Sepi:**
    * **Tindakan:** Fokuskan anggaran promosi dan kampanye *bundling* di Q1 (Januari-Februari) untuk merangsang permintaan selama periode penjualan terendah.

## Hasil Model Prediktif

Tiga model machine learning telah dibangun dan disimpan di folder `/models`:

1.  **Model Regresi (Prediksi Profit):**
    * **Tujuan:** Memprediksi *jumlah* profit (dalam USD) dari sebuah transaksi.
    * **Hasil:** Model ini dapat memprediksi profit dengan rata-rata error sekitar $... (Isi dengan nilai RMSE Anda) dan R-squared ... (Isi dengan nilai R2 Anda).

2.  **Model Klasifikasi (Prediksi Status Profit):**
    * **Tujuan:** Memprediksi apakah sebuah transaksi akan 'Menguntungkan' atau 'Merugi'.
    * **Hasil:** Model ini memiliki akurasi **...%** (Isi dengan Akurasi Anda) di data tes.

3.  **Model Time Series (Prediksi Sales):**
    * **Tujuan:** Memprediksi total penjualan bulanan untuk 6 bulan ke depan.
    * **Hasil:** Model berhasil memprediksi tren dan pola musiman penjualan (Lihat: `reports/figures/9_ts_final_forecast.png`).