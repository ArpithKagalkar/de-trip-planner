import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from project root

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def ensure_config() -> None:
    """
    Fail fast if critical config is missing.
    Call this once on startup.
    """
    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Put it into your .env file."
        )
