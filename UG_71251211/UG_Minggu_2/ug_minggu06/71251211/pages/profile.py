import streamlit as st
from user import user_data_by_username

# CEK APAKAH SUDAH LOGIN
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

user = user_data_by_username()
username = st.session_state.username

st.title("Profile")
# hint untuk mematikan text input ada di -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# BUAT 2 INPUT TEXT 1 Username 1 Password namun disable/matikan field Username dan yang password harus tipe password
st.text_input("Username", value=username, disabled=True)
password_lama = st.text_input("Password Lama", type="password")
password_baru = st.text_input("Password Baru", type="password")

# Silahkan kalau mau baca baca ini hehe ga wajib ya-> https://discuss.streamlit.io/t/buttons-alignment/51929

col1, space, col2 = st.columns([1,3,1])
with col1:
    # Buat tombol logout st.button("logout", type="primary") keluar ke app.py
    if st.button("Logout", type="primary"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.switch_page("app.py")

        
with col2:
    if st.button("Ganti Data", type="secondary", width=400):
        password_lama = user[username]["password"]

        if password_lama == "":
            st.error("Password lama tidak boleh kosong")
        elif password_baru == password_lama:
            st.error("ga boleh sama wok")
        elif password_baru == "":
            st.error("Password baru tidak boleh kosong")    
        else:
            user[username]["password"] = password_baru
            st.success("Berhasil")

    # Ini untuk ubah password st.button("Ganti Data", type="secondary", width=400)
    # Kondisi -> Password baru dan lama ga boleh sama 
    # Jika sama -> st.error("ga boleh sama wok")
    # jika beda ubah melalui variabel 'user' lalu tampilkan st.success("Berhasil")
