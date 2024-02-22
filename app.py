import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Chit Chat with PDFs", page_icon=":books:")
    st.header("Chit Chat with PDFs :books:")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload Your PDFs here and click on 'Process' ", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):

                # This gets pdf text

                # THis gets the text chunks

                # This creates vector store

if __name__ == '__main__':
    main()