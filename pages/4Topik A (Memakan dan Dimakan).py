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

# Mulai Title
st.title("TOPIK A (MEMAKAN DAN DIMAKAN)")
st.write("---")

tab1, tab2 = st.tabs(["MATERI TOPIK A", "KUIS TOPIK A"])

with tab1:
    st.header("Rantai Makanan dan Jaring-jaring Makanan")
    st.write("---")
    st.image("https://64.media.tumblr.com/fd0df2dd01829388f3ec810cc2133b53/9e59a35d4432ad71-03/s640x960/6b0cb9e6d39d9ca9ab42bc42754a77c6f18a6900.pnj")
    st.subheader("Apa maksud dari gambar di atas?")
    st.write("Charlie dan Zayn sedang berkeliling kebun dan mereka melihat seekor laba-laba yang akan memakan belalang. Charlie berinisiatif untuk menyelamatkan belalang, tetapi Zayn mencegah Charlie karena takut laba-laba akan kelaparan jika tidak memangsa belalang.")
    st.write("Hubungan makan dan dimakan dalam makhluk hidup akan membentuk rantai makanan dan jaring-jaring makanan.")
    submit = st.button("Rantai makanan dan jaring-jaring makanan?  \u2193")
    if submit:
        tab3, tab4 = st.tabs(["Rantai Makanan", "Jaring-jaring Makanan"])
        with tab3:
            st.write("Rantai makanan adalah peristiwa makan dan dimakan antara mahluk hidup dengan urutan tertentu.")
            st.write("Perhatikan gambar rantai makanan berikut!")
            st.image('https://64.media.tumblr.com/36b6e9dc168ac0b4e97299ab1b359699/cfd596d6c39762e1-aa/s500x750/c8e9ce97955741a80a7be244d3e1b693c844aebe.pnj')
            st.write("Sederhananya, kita dapat menggambarkan dalam bentuk rantai makanan sebagai berikut.")
            st.write("Rumput → Belalang → Tikus → Ular → Elang → Jamur ")
            st.write("Pada rantai makanan diatas, kita dapat melihat alur makan sebagai berikut:")
            st.write("a. Rumput sebagai produsen")
            st.write("b. Belalang sebagai konsumen tingkat 1")
            st.write("c. Tikus sebagai konsumen tingkat 2")
            st.write("d. Ular sebagai konsumen tingkat 3")
            st.write("e. Burung elang sebagai konsumen tingkat 4")
            st.write("f. Jamur sebagai dekomposer")
            st.write("Dekomposer tidak selalu berada setelah konsumen puncak dalam rantai makanan, karena dekomposer dapat berada dalam setiap tingkatan selama ada senyawa organik yang bisa diuraikan.")
                    
            with st.expander("Contoh rantai makanan"):
                st.write("Berikut beberapa contoh rantai makanan")
                st.image('https://64.media.tumblr.com/2b6bb79a18e5df072e88a650add260f9/f566c5f256d57d2b-93/s540x810/ff0f792dee6dd495ad5f3a68de0f247afda58bbd.pnj', 'Rantai makanan di laut')
                st.image('https://i0.wp.com/rumushitung.com/wp-content/uploads/2020/05/sawah.jpg?w=540&ssl=1', 'Rantai makanan di sawah')
                st.image('https://64.media.tumblr.com/872d9db9a3bece93ae2e4dce2d4c3b10/2b3ef267959d7dde-2f/s250x400/f6c7d168985db994b0af04d8af36e7bbe8b0f828.pnj', 'Rantai makanan yang pendek')
                
                                
        with tab4:
            st.image('https://64.media.tumblr.com/df02847b4fed917e5ad4e7cb814c75b7/ec7ed2f221b6f43b-60/s540x810/876efabd66e444c2081245132732a61d7a5bbfa7.pnj')
            st.write("Jaring-jaring makanan adalah sekumpulan rantai makanan yang saling berhubungan. Jaring-jaring makanan dibentuk dari beberapa rantai makanan.")
            st.write("---")
            st.write("Perhatikan contoh jaring-jaring makanan berikut!")
            st.image('https://64.media.tumblr.com/bccc843de5e622477a542bf68b6ed9c5/fb5377e50b8afd60-e3/s1280x1920/8a06b0c26599a059da36d842d32b256622478cf9.jpg')
            st.write("Umumnya, di dalam suatu ekosistem tidak hanya terdiri atas satu rantai makanan. Hal ini karena konsumen tingkat 1 dapat memakan berbagai produsen. Satu jenis produsen juga dapat dimakan oleh berbagai macam konsumen tingkat 1. Begitu pula dengan konsumen tingkat 2 dan 3 yang bisa memakan berbagai jenis hewan.")
            st.write("Oleh karena itu, pada suatu ekosistem hubungan makan dan dimakan digambarkan dengan jaring-jaring makanan yang merupakan kumpulan dari beberapa rantai makanan.")
            
            
        st.write("---")
        st.write("---")
        st.write("Untuk lebih memahami materi mengenai rantai makanan dan jaring-jaring makanan, Mari baca lebih lanjut [Bahan Ajar Selengkapnya](https://docs.google.com/document/d/1i4m7lnETG3fzwT0AQ76Ojn-jy_Vx77M2_W6I4tzV17Q/edit?usp=sharing) dan amati video berikut ini!")
        st.video("https://youtube.com/watch?v=Hlloahtfe7o&feature=share")
        st.write("---")
        st.write("Nah setelah kalian mempelajari bahan ajar dan mengamati video pembelajaran tersebut, tentu sekarang kalian sudah paham tentang Rantai makanan dan Jaring-jaring makanan")
        st.write("Untuk mengukur pemahaman kalian, mari kerjakan kuis dengan menekan tombol KUIS TOPIK A pada bagian atas   ⬆⬆⬆")
        
#Kuis
with tab2:
    st.header("Kuis Topik A")
    st.write("Untuk mengukur pemahaman kamu mengenai materi Topik A (Memakan dan Dimakan). Kerjakanlah kuis berikut dengan semangat!")
    st.write("---")
    st.subheader("[<< Klik disini untuk mengerjakan kuis >>](https://docs.google.com/forms/d/e/1FAIpQLSf6bP7x6QUqE2ZZhx7eah3HnMMg2oIgte0GWfB_q-dCRDk3_Q/viewform?usp=sf_link)")


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
   want_to_pemb = st.button("Next   \u25B6   Topik B (Transfer Energi Antarmakhluk Hidup)")
if want_to_pemb:
   switch_page("Topik B (Transfer Energi Antarmakhluk Hidup)")
