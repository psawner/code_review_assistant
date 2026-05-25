from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    # === LLM Config ===
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "meta-llama/llama-4-scout-17b-16e-instruct")

    # === Request Config ===
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", 8))

    #Github Token
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

settings = Settings()

