import streamlit as st
import preprocessor

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    # now we can convert stream data to string data
    data = bytes_data.decode("utf-8")

    df = preprocessor.preprocess(data)

    st.dataframe(df)

    # fetch unique users