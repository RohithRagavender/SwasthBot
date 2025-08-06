from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def get_relevant_docs(query, persist_dir="db"):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",  # ✅ match this with embedder
        model_kwargs={"device": "cuda"}  # or "cpu" if no GPU
    )
    db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3})
    return retriever.get_relevant_documents(query)
