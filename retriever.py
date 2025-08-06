from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def get_relevant_docs(query, persist_dir="db"):
    db = Chroma(persist_directory=persist_dir, embedding_function=HuggingFaceEmbeddings())
    retriever = db.as_retriever(search_kwargs={"k": 3})
    return retriever.get_relevant_documents(query)
