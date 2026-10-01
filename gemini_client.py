import os
from functools import lru_cache

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiError(RuntimeError):
    pass


@lru_cache(maxsize=1)
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise GeminiError(
            "GEMINI_API_KEY is not configured. "
            "Please add it to your .env file."
        )

    return genai.Client(api_key=api_key)


def generate_text(prompt: str) -> str:
    client = get_client()

    model = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        if not response or not response.text:
            raise GeminiError(
                "Gemini returned an empty response."
            )

        return response.text.strip()

    except Exception as exc:
        raise GeminiError(
            f"Gemini request failed: {exc}"
        ) from exc