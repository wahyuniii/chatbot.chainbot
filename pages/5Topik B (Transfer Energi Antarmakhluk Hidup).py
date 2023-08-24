import streamlit as st

# Menghilangkan tombol Menu
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Mengganti Background dengan gambar
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://64.media.tumblr.com/f1b799a9001ef3c5039b8c2df732302a/bee820355e1c5385-b5/s500x750/087d44811a92dbcaaead66ac876d8a0e9258e9d5.pnj");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba{0, 0, 0, 0};
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebar"] {
background-image: url("https://64.media.tumblr.com/f03e5348421e425537094271ae34744d/223b78955680fc84-d2/s1280x1920/a91533545bb5831958da980be2534e824397fb99.pnj");
background-size: cover;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Pilihan Ganda
st.title("TOPIK B (TRANSFER ENERGI ANTARMAKHLUK HIDUP)")

tab1, tab2 = st.tabs(["Transfer Energi Antarmakhluk Hidup", "KUIS TOPIK B"])

with tab1:
    st.header("Transfer Energi Antarmakhluk Hidup")
    st.write("---")
    st.image("https://64.media.tumblr.com/851a17f747284052116b81ce81fad611/7b5d04a0a9f9cd60-bf/s540x810/65a7beb65c88cb0ff3a0ec382d857d91fae4cda1.pnj")
    st.subheader("Bagaimana transfer energi yang terjadi pada suatu ekosistem?")
    st.write("Rantai makanan menggambarkan jalur alur energi yang ada pada suatu ekosistem.")
    st.write("Para saintis memperkirakan energi yang digunakan oleh makhluk hidup sebesar 90%. Artinya, hanya ada 10% sisa energi yang bisa dikonsumsi oleh makhluk hidup lain melalui transfer energi.")
    st.write("Transfer energi dapat digambarkan dalam bentuk piramida makanan.")
    with st.expander("Piramida Makanan"):
        st.subheader("Piramida Makanan")
        st.image('https://64.media.tumblr.com/2d7e51b1b18cd72168ddf925d49c75b5/47777aaa2a98d776-45/s540x810/81877e03756f0fca2dcdef183f10de36cebd1392.pnj', 'Gambar piramida makanan')
        st.write("Pada piramida makanan, semakin rendah tingkatannya akan semakin banyak jumlah tumbuhan atau hewan yang termasuk di dalamnya. Sebaliknya, semakin tinggi tingkatannya, maka semakin besar ukuran dan semakin sedikit jumlah hewan yang termasuk di dalamnya.")
        st.write("Dekomposer tidak digambarkan dalam piramida ini karena dekomposer dapat berada dalam setiap tingkatan selama ada senyawa organik yang bisa diuraikan.")
        st.write("---")
        st.write("Untuk lebih memahami materi mengenai transfer energi, Mari baca lebih lanjut [Bahan Ajar Selengkapnya](https://docs.google.com/document/d/1ZGMHIbYWM9dl4WJClQp8-9xraw79_-XFNbxDEUF_neI/edit?usp=sharing) dan simak video pembelajaran berikut.")
        st.video("https://youtube.com/watch?v=CGVcKH2LZCM&feature=share")
        st.write("---")
        st.write("Nah, setelah membaca bahan ajar dan mengamati video pembelajaran tersebut, berarti kamu telah memahami tentang transfer energi. Sekarang cobalah lakukan percobaan transfer energi berikut!")
        submit = st.button("Percobaan tentang Transfer Energi   \u2193")
        if submit:
            st.write("Lakukan percobaan proses transfer energi pada jaring-jaring makanan berikut secara berkelompok.")
            st.image("https://64.media.tumblr.com/f3876bbefe4c27292ef8e65222a6ac1e/eb4629e1d6c5670a-4e/s2048x3072/8eee55d28a4447d01db533159197854c8ad09805.pnj")
            st.write("---")
            st.write("Untuk memahami langkah-langkah percobaan, simak video berikut!")
            st.video("https://youtu.be/Exa2ns600WY")
        st.write("---")
        st.write("---")
        st.write("Untuk mengukur pemahaman kamu mengenai transfer energi, mari kerjakan kuis dengan menekan tombol KUIS TOPIK B pada bagian atas   ⬆⬆⬆")


# KUIS
with tab2:
    st.header("Kuis Topik B")
    st.write("Untuk mengukur pemahaman kamu mengenai materi Topik B (Transfer Energi Antarmakhluk Hidup). Kerjakanlah kuis berikut dengan semangat!")
    st.write("---")
    st.subheader("[<< Klik disini untuk mengerjakan kuis >>](https://docs.google.com/forms/d/e/1FAIpQLSeAC8TQ2oLGe-mhxr-QkihZ-JtFVZJrMHL8GUFJfj1V-WWMBw/viewform?usp=sf_link)")


#Ganti Page Berdampingan
st.markdown(
    """
    <style>
    .stButton button {
        font-size: 18px;
        background-color: #ff8c00; /* Ubah dengan kode warna coklat pastel yang diinginkan */
        color: white;
        width:100%
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("---")
st.write("---")
st.write("---")

from streamlit_extras.switch_page_button import switch_page

col1, col2= st.columns(2)
with col1:
   want_to_menu = st.button("\u25C0   Menu")
if want_to_menu:
   switch_page("Menu")
 
with col2:
   want_to_pemb = st.button("Next   \u25B6   Tentang Pengembang")
if want_to_pemb:
   switch_page("Tentang Pengembang")
