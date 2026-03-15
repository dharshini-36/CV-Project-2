import streamlit as st
import cv2
import numpy as np
from PIL import Image

from cartoon_filter import cartoonify
from meme_generator import create_meme

st.title("🎭 OpenCV Fun Editor")

option = st.sidebar.selectbox(
    "Choose Feature",
    ["Cartoon Selfie Camera", "AI Meme Generator"]
)

uploaded_file = st.file_uploader("Upload an Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    image = np.array(image)

    st.image(image, caption="Original Image", use_column_width=True)

    if option == "Cartoon Selfie Camera":

        if st.button("Apply Cartoon Filter"):

            cartoon = cartoonify(image)

            st.image(cartoon, caption="Cartoon Image")

            result = Image.fromarray(cartoon)
            st.download_button(
                "Download Image",
                data=result.tobytes(),
                file_name="cartoon.png"
            )

    elif option == "AI Meme Generator":

        text = st.text_input("Enter Meme Caption")

        if st.button("Generate Meme"):

            meme = create_meme(image.copy(), text)

            st.image(meme, caption="Meme Image")

            result = Image.fromarray(meme)

            st.download_button(
                "Download Meme",
                data=result.tobytes(),
                file_name="meme.png"
            )
