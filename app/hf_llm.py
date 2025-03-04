from huggingface_hub import InferenceClient
from langchain.llms.base import LLM
from typing import List
from config import HF_API_KEY, LLM_MODEL, LLM_PROVIDER, SYSTEM_PROMPT

client = InferenceClient(
    model=LLM_MODEL,
    api_key=HF_API_KEY,
    provider=LLM_PROVIDER)

class HuggingFaceLLM(LLM):
    """
    Custom LLM wrapper for Hugging Face API
    """
    def _call(self, prompt: str, stop: List[str] = None) -> str:
        """Calls the Hugging Face model with correct JSON structure"""
        response = client.chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=512
        )
        return response.get("choices", [{}])[0].get("message", {}).get("content", "Error: No response")

    @property
    def _llm_type(self) -> str:
        return "huggingface_api"
