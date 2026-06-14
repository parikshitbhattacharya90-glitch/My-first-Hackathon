import streamlit as st


st.set_page_config(layout="wide")
st.title('INDIA Redob Hackathon')

resume = st.file_uploader("Upload your resume",type = "pdf")

if resume:
    b = st.button("Start analysis")

