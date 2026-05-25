from langchain_groq import ChatGroq
from src.config.settings import settings

def get_model():
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.MODEL_NAME,
        temperature=0.1,
        max_tokens=100,
    )