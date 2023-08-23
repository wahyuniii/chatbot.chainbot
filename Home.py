import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.stateful_button import button


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
st.title("HALO DENGAN CHAINBOT DISINI :wave:")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets6.lottiefiles.com/packages/lf20_gaj4x0te.json"
lottie_html = f'<div class="lottie" style="background-color: #FF000;"><lottie-player src="{lottie_url_hello}" background="transparent" speed="1" loop autoplay></lottie-player></div>'
st.markdown(lottie_html, unsafe_allow_html=True)
lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="hello")

# Menambahkan CSS untuk mengatur teks menjadi rata tengah, besar, dan latar belakang teks
import streamlit as st


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.markdown(
    """
    <style>
    .my-text {
        font-size: 16px;
    }
    .stTextInput input {
        background-color: #FFAE69;
    }
    .stTextInput label {
        font-size: 20px;
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="my-text">Untuk mulai belajar, tuliskan Namamu pada kolom dibawah ini kemudian tekan Submit  \u2193  \u2193  \u2193</p>', unsafe_allow_html=True)

my_input = st.text_input(st.session_state["my_input"])

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.markdown(f"Selamat datang **{my_input}**, Chainbot siap menemani belajarmu")
    st.write("Sebelum memulai belajar, bacalah petunjuk penggunaan Chainbot terlebih dahulu ya")
    st.image("https://64.media.tumblr.com/b53136b7fcfabe2cfea621e157f720ef/d3fb9f2d7ab2025d-7c/s400x600/81cb44100d827c3bffdc70d05115dadcddbdaee4.pnj")

# Tulis
