import streamlit as st
from PIL import Image
from dotenv import load_dotenv

from transformers import pipeline


def load_model_blip():
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")


pipe = load_model_blip()


def main():
    load_dotenv()

    stream = True

    st.title("Image Captioning with BLIP")

    with open("./tasks/utils/description/image_captioning_desc.txt", "r") as file:
        description = file.read()
    st.markdown(description)

    sample_image_path = "./tasks/utils/sample/sample_ic_dog.jpeg"
    sample_image = Image.open(sample_image_path)
    st.image(sample_image, caption="Sample Image for Image Captioning", use_column_width=True)

    if st.button("Process"):
        with st.spinner("======== Sending request to API.. ========"):
            output = pipe(sample_image)
            st.write(output)


    st.header("💡 Try with your own image file")
    st.write(
            """
            Try testing the model with your own iamge file. 
            """
            )

                        

    uploaded_file = st.file_uploader("Upload an image", type=["jpeg", "jpg", "png"])

    print("Opening image file...")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(uploaded_file, caption="Uploaded Image", use_column_width = True)

        if st.button("Process"):
            with st.spinner("======== Sending request to API.. ========"):          
              output = pipe(image)
              st.write(output)











