from gemini_client import generate_text


def summarize_text(text: str) -> str:
    try:
        prompt = f"""
Summarize the following text in simple language.

Keep the important information.
Make the summary concise and easy to understand.

Text:
{text}
"""
        return generate_text(prompt)

    except Exception:
        # Temporary demo fallback when Gemini quota is unavailable
        return (
            "Demo Summary:\n\n"
            "This text explains the main idea of the given topic "
            "in a simple and concise way. The important information "
            "has been summarized for easy understanding."
        )