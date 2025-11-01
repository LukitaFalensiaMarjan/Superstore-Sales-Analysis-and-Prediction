import streamlit as st
import pandas as pd
import joblib
import os

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Superstore Profit Predictor",
    page_icon="📈",
    layout="centered"
)

# --- Path ke Model ---
# (Pastikan app.py ada di root folder, sejajar dengan folder 'models')
MODEL_PATH = "models/"
REG_MODEL_FILE = os.path.join(MODEL_PATH, "1_regression_profit_predictor.joblib")
REG_PREPROC_FILE = os.path.join(MODEL_PATH, "1_preprocessor_reg.joblib")
CLS_MODEL_FILE = os.path.join(MODEL_PATH, "2_classification_profit_predictor.joblib")
CLS_PREPROC_FILE = os.path.join(MODEL_PATH, "2_preprocessor_cls.joblib")

# --- Fungsi untuk Memuat Model (dengan Cache) ---
# st.cache_data menyimpan model di memori, jadi tidak perlu di-load ulang setiap kali
@st.cache_data
def load_model(model_file, preproc_file):
    """Memuat model dan preprocessor dari file."""
    try:
        model = joblib.load(model_file)
        preprocessor = joblib.load(preproc_file)
        return model, preprocessor
    except FileNotFoundError:
        st.error(f"Error: File model atau preprocessor tidak ditemukan. Pastikan file ada di folder '{MODEL_PATH}'.")
        return None, None
    except Exception as e:
        st.error(f"Terjadi error saat memuat model: {e}")
        return None, None

# --- Muat Model ---
model_reg, preprocessor_reg = load_model(REG_MODEL_FILE, REG_PREPROC_FILE)
model_cls, preprocessor_cls = load_model(CLS_MODEL_FILE, CLS_PREPROC_FILE)

# --- UI (User Interface) Aplikasi ---
st.title("📈 Superstore Profit Predictor")
st.write("Masukkan detail transaksi untuk memprediksi profit dan status profitabilitas.")

# --- Input ditaruh di Sidebar ---
st.sidebar.header("Masukkan Detail Transaksi:")

# Input Kategori (Dropdown)
# Ambil dari data unik Anda
category_options = ['Furniture', 'Office Supplies', 'Technology']
category = st.sidebar.selectbox("Pilih Kategori:", category_options)

# Input Region (Dropdown)
# Ambil dari data unik Anda
region_options = ['South', 'West', 'Central', 'East']
region = st.sidebar.selectbox("Pilih Region:", region_options)

# Input Kuantitas (Angka)
quantity = st.sidebar.number_input("Jumlah Kuantitas:", min_value=1, max_value=20, value=2, step=1)

# Input Diskon (Slider)
discount = st.sidebar.slider("Pilih Diskon:", min_value=0.0, max_value=0.8, value=0.0, step=0.05)

# --- Tombol Prediksi ---
if st.sidebar.button("Prediksi Profit 🚀"):
    
    if model_reg and preprocessor_reg and model_cls and preprocessor_cls:
        
        # --- 1. Persiapan Data untuk Model Regresi ---
        # Buat DataFrame dari input (harus 2D)
        data_reg = pd.DataFrame({
            'Category': [category],
            'Region': [region],
            'Quantity': [quantity],
            'Discount': [discount]
        })
        
        # Proses data dengan preprocessor regresi
        X_reg_processed = preprocessor_reg.transform(data_reg)
        
        # Buat prediksi profit
        pred_profit = model_reg.predict(X_reg_processed)[0] # Ambil nilai pertama
        
        
        # --- 2. Persiapan Data untuk Model Klasifikasi ---
        data_cls = pd.DataFrame({
            'Category': [category],
            'Discount': [discount],
            'Region': [region]
        })
        
        # Proses data dengan preprocessor klasifikasi
        X_cls_processed = preprocessor_cls.transform(data_cls)
        
        # Buat prediksi status
        pred_status = model_cls.predict(X_cls_processed)[0] # Ambil nilai pertama
        
        
        # --- 3. Tampilkan Hasil ---
        st.subheader("Hasil Prediksi:")
        
        # Tampilkan Prediksi Profit
        st.metric(label="Prediksi Profit (USD)", value=f"${pred_profit:,.2f}")
        
        # Tampilkan Status Profit
        if pred_profit > 0:
            st.success("✅ Status: Transaksi ini diprediksi **Menguntungkan**.")
        else:
            st.error("❌ Status: Transaksi ini diprediksi **Merugi**.")
            
    else:
        st.error("Model tidak berhasil dimuat. Periksa kembali path file Anda.")

st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 lukifm17 | All rights reserved.")