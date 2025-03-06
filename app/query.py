from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from app.embeddings import get_embeddings_model
from app.hf_llm import HuggingFaceLLM


# Initialize custom Hugging Face LLM suitable for RAG pipeline
hf_llm = HuggingFaceLLM()

# Load FAISS index
faiss_index = FAISS.load_local(
    "faiss_index",
    get_embeddings_model(),
    allow_dangerous_deserialization=True
    )

# Create retriever
retriever = faiss_index.as_retriever()

# Define RAG pipeline using created LLM and retriever
rag_chain = RetrievalQA.from_chain_type(
    llm=hf_llm,
    chain_type="stuff",
    retriever=retriever
)

def rag_query(question: str):
    response = rag_chain.invoke({"query": question})
    return response.get("result")
