# models/llm.py
import os
from langchain_community.chat_models import ChatOllama
from langchain.chat_models import init_chat_model


def get_llm():
    provider = os.getenv("LLM_PROVIDER","ollama")
    if provider=="ollama":
        # arranca: `ollama run mistral:7b-instruct-q4`
        return ChatOllama(model=os.getenv("OLLAMA_MODEL","mistral:7b-instruct-q4"), temperature=0.2)
    # genérico vía API (OpenAI/Bedrock/etc.) con LCEL:
    return init_chat_model(os.getenv("API_MODEL","gpt-4o-mini"), model_provider=os.getenv("PROVIDER","openai"), temperature=0.2)
