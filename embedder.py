from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


def embed_docs(docs, persist_dir="db"):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cuda"}  # 👈 Uses GPU
    )
    vectordb = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=persist_dir)
    vectordb.persist()
    return vectordb
