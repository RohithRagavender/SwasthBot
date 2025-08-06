
# 🩺 SwasthBot.ai – Smart Medical Assistant (RAG Project)

**SwasthBot.ai** is a lightweight, AI-powered medical chatbot that can read and understand medical documents (PDFs) and answer user questions intelligently.

This project uses **Retrieval-Augmented Generation (RAG)** with **LangChain**, **ChromaDB**, and **HuggingFace Transformers**, packaged in a beautiful interactive **Streamlit UI** — with chat history, dark mode, and more!

---

## 🚀 Live Demo
🔗 [https://swasthbot.onrender.com](https://swasthbot.onrender.com)

---

## 🧠 What Can It Do?

✅ Upload one or more **medical PDFs**  
✅ Ask natural-language **questions**  
✅ Get **accurate, summarized answers**  
✅ Clean **chat UI** with history  
✅ Toggle between **Light and Dark Mode**

---

---

## 🛠️ Tech Stack

| Layer       | Technology                      |
|------------|----------------------------------|
| UI         | [Streamlit](https://streamlit.io) |
| Embeddings | [SentenceTransformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) |
| Vector DB  | [ChromaDB](https://www.trychroma.com/) |
| LLM        | [Flan-T5](https://huggingface.co/google/flan-t5-base) or TinyLlama |
| RAG Engine | [LangChain](https://www.langchain.com/) |
| File Input | PDF via [PyPDFLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf/) |

---

## 📁 Project Structure

```

swasthbot/
├── app.py                   # Streamlit frontend (with chat + dark mode)
├── loader.py                # Load and split PDF
├── embedder.py              # Embed docs and store in ChromaDB
├── retriever.py             # Semantic search logic
├── llm\_chain.py             # LLM + Prompt logic
├── data/
│   └── medical\_guides/      # Folder for uploaded PDFs
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/RohithRagavender/SwasthBot.git
cd SwasthBot
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app locally

```bash
streamlit run app.py
```

---

## 🧪 Test the Bot

Upload PDFs like:

* `First Aid Guidelines`
* `Govt Health Scheme`
* `Common Disease Prevention`

Ask questions like:

* *"What is the treatment for fever?"*
* *"Precautions for malaria?"*
* *"How to handle burns?"*

---

## 🧰 Requirements

* Python 3.9 or higher
* Chrome / Firefox browser
* For GPU support, install CUDA-enabled PyTorch & use `"device": "cuda"`

---

## 🧠 How RAG Works (Simplified)

1. **PDF Loader** → Breaks into readable chunks
2. **Embeddings** → Converts text to vectors
3. **ChromaDB** → Stores vectorized content
4. **Retriever** → Fetches relevant chunks
5. **LLM (Flan-T5)** → Generates the final answer
6. **Streamlit** → Shows result in chat UI

---

## 🎯 Why This Project?

✅ Demonstrates skills in **AI, NLP, and UI**
✅ Shows **LangChain + RAG** understanding
✅ Clean **codebase + professional UI**
✅ Ideal for **Data Science / AI Engineer jobs**

---

## 🧑‍💼 Author

**Rohith Ragavender**
🔗 [GitHub](https://github.com/RohithRagavender)
💼 Aspiring AI Engineer | Full Stack Developer

---

## 📌 Future Enhancements

* 🔲 Summarize entire PDF
* 🔲 Multilingual (Tamil, Hindi)
* 🔲 Export chat history
* 🔲 PDF source highlighting
* 🔲 Frontend in React (for HuggingFace deployment)

---

