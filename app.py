import streamlit as st
import cv2
import numpy as np
from PIL import Image

from cartoon_filter import cartoonify
from meme_generator import create_meme

st.title("🎭 AI Cartoon & Meme Generator")

option = st.sidebar.selectbox(
    "Choose Feature",
    ["Cartoon Selfie Camera", "AI Meme Generator"]
)

input_method = st.radio(
    "Select Input Method",
    ["Upload Image", "Use Webcam"]
)

image = None

# Upload Image
if input_method == "Upload Image":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        image = np.array(image)

# Webcam Capture
elif input_method == "Use Webcam":
    camera_image = st.camera_input("Take a picture")
    if camera_image:
        image = Image.open(camera_image)
        image = np.array(image)

if image is not None:

    st.image(image, caption="Original Image", use_column_width=True)

    if option == "Cartoon Selfie Camera":

        if st.button("Apply Cartoon Filter"):
            cartoon = cartoonify(image)
            st.image(cartoon, caption="Cartoon Image")

            result = Image.fromarray(cartoon)
            st.download_button(
                "Download Cartoon Image",
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
