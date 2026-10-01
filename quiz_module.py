from gemini_client import generate_text
import json
import re


def generate_quiz(topic: str):

    try:
        prompt = f"""
Create a quiz about {topic}.

Create exactly 3 multiple-choice questions.

Each question must have:
- One question
- Four options
- One correct answer

Return ONLY valid JSON.

Use exactly this format:

[
    {{
        "question": "Question here",
        "options": [
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "answer": "Option A"
    }}
]
"""

        result = generate_text(prompt)

        result = re.sub(r"```json", "", result, flags=re.IGNORECASE)
        result = re.sub(r"```", "", result)
        result = result.strip()

        quiz = json.loads(result)

        if not isinstance(quiz, list):
            raise ValueError("Quiz response is not a list.")

        return quiz

    except Exception:
        # Temporary demo fallback when Gemini quota is unavailable
        return [
            {
                "question": "What is Artificial Intelligence?",
                "options": [
                    "A technology that enables machines to perform intelligent tasks",
                    "A type of computer cable",
                    "A programming keyboard",
                    "A database"
                ],
                "answer": "A technology that enables machines to perform intelligent tasks"
            },
            {
                "question": "Which is an example of AI?",
                "options": [
                    "Voice assistant",
                    "Notebook",
                    "Chair",
                    "Water bottle"
                ],
                "answer": "Voice assistant"
            },
            {
                "question": "What can AI learn from?",
                "options": [
                    "Data",
                    "Paper only",
                    "Electricity only",
                    "Nothing"
                ],
                "answer": "Data"
            }
        ]