from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

def get_embeddings_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L6-v2")

def create_faiss_index():
    # Load CV from .txt file
    text_loader = TextLoader("./data/cv.txt")
    document = text_loader.load()

    # Extract the text from Document object
    text = "".join([doc.page_content for doc in document])

    # Split text into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = text_splitter.split_text(text)

    # Convert chunks to Document objects
    chunks = [Document(page_content=chunk) for chunk in chunks]

    # Get embeddings model
    embeddings_model = get_embeddings_model()

    # Create FAISS index
    faiss_index = FAISS.from_documents(chunks, embeddings_model)
    faiss_index.save_local("faiss_index")

if __name__ == "__main__":
    create_faiss_index()
