from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFacePipeline

def build_chain():
    prompt = PromptTemplate.from_template(
        "You are a helpful medical assistant.\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    )
    llm = HuggingFacePipeline.from_model_id(
        model_id="google/flan-t5-base",
        task="text2text-generation"
    )
    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)
    return chain
