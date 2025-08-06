from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

def build_chain():
    prompt = PromptTemplate.from_template(
        "You are a helpful medical assistant.\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    )

    pipe = pipeline("text2text-generation",
                    model="google/flan-t5-base",
                    device=0)  # 👈 GPU device ID

    llm = HuggingFacePipeline(pipeline=pipe)
    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)
    return chain
