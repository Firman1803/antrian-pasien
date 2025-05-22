import streamlit as st

# Simpan antrian di session state (agar tidak reset setiap refresh)
if "queue" not in st.session_state:
    st.session_state.queue = []

st.title("Aplikasi Antrian Pasien")

# Form input pasien baru
with st.form("add_patient_form"):
    patient_name = st.text_input("Nama Pasien")
    submitted = st.form_submit_button("Tambahkan ke Antrian")
    if submitted and patient_name:
        st.session_state.queue.append(patient_name)
        st.success(f"{patient_name} berhasil ditambahkan ke antrian!")

# Tampilkan antrian
st.subheader("Daftar Antrian")
if st.session_state.queue:
    for i, name in enumerate(st.session_state.queue, start=1):
        st.write(f"{i}. {name}")
else:
    st.info("Antrian kosong.")

# Tombol panggil pasien
if st.button("Panggil Pasien Selanjutnya"):
    if st.session_state.queue:
        next_patient = st.session_state.queue.pop(0)
        st.success(f"Memanggil pasien: {next_patient}")
    else:
        st.warning("Tidak ada pasien dalam antrian.")
