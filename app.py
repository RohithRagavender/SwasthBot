import streamlit as st
import os
from loader import load_and_split_docs
from embedder import embed_docs
from retriever import get_relevant_docs
from llm_chain import build_chain

# 🌟 Styling
st.set_page_config(page_title="SwasthBot.ai", page_icon="🩺")
st.markdown(
    """
    <style>
    .main { background-color: #f9fcff; }
    .block-container { padding: 2rem 2rem; }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 16px;
        font-size: 16px;
        border-radius: 8px;
    }
    .response-box {
        background-color: #eef7ff;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #cce5ff;
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🩺 Title
st.title(" SwasthBot.ai – Your Smart Medical Assistant")

# 📁 Upload PDF(s)
pdfs = st.file_uploader(" Upload Medical PDFs (e.g., First Aid, Govt Schemes)", type="pdf", accept_multiple_files=True)

# 🧠 Load and Embed
if pdfs:
    all_docs = []
    os.makedirs("data/medical_guides", exist_ok=True)

    with st.spinner("🔄 Processing PDFs..."):
        for pdf in pdfs:
            file_path = f"data/medical_guides/{pdf.name}"
            with open(file_path, "wb") as f:
                f.write(pdf.read())
            chunks = load_and_split_docs(file_path)
            all_docs.extend(chunks)

        embed_docs(all_docs)

    st.success("✅ Documents processed and embedded!")

# ❓ Ask a Question
query = st.text_input("💬 Ask something based on your uploaded documents:")

if query:
    with st.spinner("Thinking..."):
        chain = build_chain()
        relevant_docs = get_relevant_docs(query)
        response = chain.run(input_documents=relevant_docs, question=query)

    st.markdown(f"<div class='response-box'>🧠 <b>Answer:</b><br>{response}</div>", unsafe_allow_html=True)
