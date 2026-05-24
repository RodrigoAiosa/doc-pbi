import streamlit as st
from services.pbix_extractor import PBIXExtractor
from services.pbix_parser import PBIXParser
from services.documentation_generator import DocumentationGenerator


st.set_page_config(
    page_title="Power BI Documenter",
    layout="wide"
)


with open("styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


st.title("📘 Power BI Documentation Generator")

st.write(
    "Faça upload do arquivo .pbix para gerar a documentação automática"
)

uploaded_file = st.file_uploader(
    "Upload do arquivo PBIX",
    type=["pbix"]
)


if uploaded_file:

    with st.spinner("Processando arquivo PBIX..."):

        pbix_path = "temp.pbix"

        with open(pbix_path, "wb") as f:
            f.write(uploaded_file.read())

        extractor = PBIXExtractor(pbix_path)

        extraction_result = extractor.extract()

        if not extraction_result["success"]:
            st.error(extraction_result["error"])
            st.stop()

        parser = PBIXParser(
            extraction_result["output_dir"]
        )

        parsed_data = parser.parse()

        generator = DocumentationGenerator()

        html_file = generator.generate_html(parsed_data)

        st.success("Documentação gerada com sucesso!")

        st.subheader("Resumo")

        st.write(parsed_data)

        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        st.download_button(
            label="📥 Download HTML",
            data=html_content,
            file_name="documentacao_powerbi.html",
            mime="text/html"
        )
