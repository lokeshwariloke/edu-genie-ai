from gemini_client import generate_text


def answer_question(question: str) -> str:
    try:
        prompt = f"""
Answer the following question clearly and simply.

Question:
{question}

Give a concise educational answer.
"""
        return generate_text(prompt)

    except Exception:
        # Temporary demo fallback when Gemini quota is unavailable
        return (
            f"Demo Answer:\n\n"
            f"{question} is an important educational topic. "
            f"It can be understood by learning its basic definition, "
            f"main concepts, and practical examples."
        )