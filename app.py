
import requests, base64
import json
import streamlit as st
from dotenv import load_dotenv
import os

from tasks import biomedical_agent
#from tasks import ocr, biomedical_agent, image_captioning




add_task = st.sidebar.radio(
    "Which task would you like to try?",
    ("Biomedical research agent", "OCR Text Extraction", "Vision-Language Image Captioning with BLIP")
)
if add_task == "Biomedical research agent":
    biomedical_agent.main()

# if add_task == "OCR Text Extraction":
#     ocr.main()

# if add_task == "Vision-Language Image Captioning with BLIP":
#     image_captioning.main()





