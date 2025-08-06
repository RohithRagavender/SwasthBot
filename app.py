import streamlit as st
from rag.loader import load_and_split_docs
from rag.embedder import embed_docs
from rag.retriever import get_relevant_docs
from rag.llm_chain import build_chain
import os

os.makedirs("data/medical_guides", exist_ok=True)
st.title("🩺 SwasthBot.ai – Smart Medical Assistant")
pdfs = st.file_uploader("📄 Upload Medical PDFs", type="pdf", accept_multiple_files=True)

if pdfs:
    all_docs = []
    for pdf in pdfs:
        file_path = f"data/medical_guides/{pdf.name}"
        with open(file_path, "wb") as f:
            f.write(pdf.read())
        docs = load_and_split_docs(file_path)
        all_docs.extend(docs)

    embed_docs(all_docs)
    st.success("✅ All PDFs Embedded Successfully!")

    query = st.text_input("❓ Ask me anything from the documents:")
    if query:
        chain = build_chain()
        relevant_docs = get_relevant_docs(query)
        response = chain.run(input_documents=relevant_docs, question=query)
        st.write("🤖", response)
