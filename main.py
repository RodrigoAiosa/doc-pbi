import streamlit as st
from pbix_extractor import PBIXExtractor

st.set_page_config(
    page_title="Power BI Documenter",
    layout="wide"
)

st.title("📘 Power BI Documentation Generator")

uploaded_file = st.file_uploader(
    "Upload do arquivo PBIX",
    type=["pbix"]
)

if uploaded_file:

    with open("temp.pbix", "wb") as f:
        f.write(uploaded_file.read())

    extractor = PBIXExtractor("temp.pbix")

    extracted = extractor.extract()

    st.success("Arquivo processado com sucesso!")
