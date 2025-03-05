# **RAG-Based CV Query API (FastAPI + FAISS + Hugging Face)**

## Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system using **FastAPI, FAISS, and Hugging Face** to allow querying a CV. It retrieves relevant text from a vector database and generates responses using a hosted LLM.

---

## Features
- **FastAPI-powered REST API** for querying a CV.
- **FAISS Vector Database** for efficient document retrieval.
- **Hugging Face Inference API** for LLM-based response generation.
- **Dockerized Deployment** for easy containerized execution.
- **Environment Variable Security** to protect sensitive API keys.

---

## **📂 Project Structure**
```
rag-cv-qa/
│── app/
│   ├── main.py               # FastAPI application
│   ├── query.py              # RAG pipeline
│   ├── embeddings.py         # Embedding model setup
│   ├── hf_llm.py             # LLM wrapper for HF model
│   ├── config.py             # Configuration file
│   ├── __init__.py           # Marks app as a Python module
│
│── data/
│   ├── cv.txt                # CV file to be indexed in
│   ├── cv.pdf                # CV file in PDF format
│
│── faiss_index/              # Stored FAISS database
│── Dockerfile                # Docker configuration
│── requirements.txt          # Python dependencies
│── .dockerignore             # Ignore sensitive files from Docker
│── README.md                 # Project documentation
│── .gitignore                # Ignore unnecessary files
```

---

## Installation & Setup
### Clone the Repository
```bash
git clone https://github.com/your-username/rag-cv-qa.git
cd rag-cv-qa
```

### Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the project root:
```bash
HF_API_KEY=your_huggingface_api_key
```

### Generate FAISS Index from CV
```bash
python app/embeddings.py
```

### Run FastAPI Locally
```bash
uvicorn app.main:app --reload
```
Open `http://localhost:8000/docs` to access the API documentation.

---

## Running with Docker
### Build the Docker Image
```bash
docker build -t rag-cv-qa .
```

### Run the Container with Environment Variables
```bash
docker run -p 8000:8000 --env-file .env rag-cv-qa
```

---

## API Endpoints
### Test API Availability
```bash
GET /
```
**Response:**
```json
{"message": "Hello, this is QA bot for my CV. Feel free to ask any questions!"}
```

### Query the CV
```bash
POST /query/?question=Do you know spark??
```
**Response:**
```json
{"answer": "Yes, I do know Spark. It is listed in my tech stack on the CV."}
```

---

## License
MIT License. Free to use and modify.


