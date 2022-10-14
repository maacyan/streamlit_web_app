import streamlit as st
from PIL import Image

st.title('サマーアプリ')
st.caption('これはさぷーの動画用のテストアプリです  ')

image = Image.open('./data/sample.png')
st.image(image, width=200)