from gemini_client import generate_text


def explain_topic(topic: str) -> str:
    try:
        prompt = f"""
Explain the following topic in simple language for a college student.

Topic:
{topic}

Give:
1. A simple definition
2. The main points
3. A small example

Keep the explanation clear and easy to understand.
"""
        return generate_text(prompt)

    except Exception:
        # Temporary demo fallback when Gemini quota is unavailable
        return (
            f"Demo Explanation:\n\n"
            f"{topic} is an important concept. "
            f"It can be understood by learning its basic definition, "
            f"main points, and a simple real-world example."
        )