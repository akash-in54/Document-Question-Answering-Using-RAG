import streamlit as st
import tempfile

from pdf_utils import load_and_split_pdf
from vectorstore import create_vectorstore
from qa_chain import get_qa_chain

st.set_page_config(
    page_title="Document Question Answering Using RAG",
    layout="wide"
)

st.title("📄 Document Question Answering Using RAG")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    with st.spinner("Processing document..."):
        chunks = load_and_split_pdf(pdf_path)
        vectorstore = create_vectorstore(chunks)
        qa_chain = get_qa_chain(vectorstore)

    question = st.text_input("Ask a question based on the document")

    if question:
        response = qa_chain.invoke(question)
        st.subheader("Answer")
        st.write(response)
