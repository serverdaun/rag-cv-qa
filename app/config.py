import os
from dotenv import load_dotenv

load_dotenv()

LLM_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"
LLM_PROVIDER = "hf-inference"
SYSTEM_PROMPT = """
    You are Vasilii Tokarev.
    You applied for a ML Engineer position and now you have to answer the questions about your CV.
    CV is provided within context.
"""
HF_API_KEY = os.getenv("HF_API_KEY")
