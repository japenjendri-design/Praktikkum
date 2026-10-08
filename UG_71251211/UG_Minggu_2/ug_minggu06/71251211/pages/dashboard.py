import streamlit as st
from user import user_data_by_username

st.set_page_config(page_title="DwTix - Dashboard")

# cek apakah sudah login -> JIKA BELUM ALIHKAN KE app.py
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")
# JANGAN PERNAH RAGU UNTUK CEK DATA PAKAI st.write() ya dari pada ngawang
data = user_data_by_username()
username = st.session_state.username
role = data[username]["role"]
# ambil role yang login dari data
if role == "Peserta":
    st.switch_page("pages/event.py")
# role = ??

# JIKA YANG LOGIN PESERTA -> ALIHKAN KE PAGE EVENT

st.title(f"Welcome, {role} 👋")

# JIKA YANG LOGIN ADMIN TAMPILKAN SELURUH DATA TERSERAH MAU BENTUKNYA APAPUN st.table, st.write boleh aja
if role == "Admin":
    st.subheader("Data Seluruh Pengguna")
    st.table(data)

    # tombol ke profile
    if st.button("Profile"):
        st.switch_page("pages/profile.py")
