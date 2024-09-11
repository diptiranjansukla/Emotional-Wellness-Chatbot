import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings = Settings()

if not settings.OPENAI_API_KEY:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")
