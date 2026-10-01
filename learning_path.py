from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    try:
        prompt = f"""
Create a learning path for the topic: {topic}

Include:
1. Beginner level
2. Intermediate level
3. Advanced level
4. Important concepts to learn
5. Practice suggestions
6. Useful resources

Keep it simple and suitable for a college student.
"""
        return generate_text(prompt)

    except Exception:
        # Temporary demo fallback when Gemini quota is unavailable
        return (
            f"Demo Learning Path for {topic}\n\n"
            "1. Beginner Level\n"
            "- Learn the basic concepts and terminology.\n\n"
            "2. Intermediate Level\n"
            "- Study the important concepts in more detail.\n"
            "- Practice with simple examples.\n\n"
            "3. Advanced Level\n"
            "- Explore advanced concepts and real-world applications.\n\n"
            "4. Practice\n"
            "- Solve exercises and build a small project.\n\n"
            "5. Resources\n"
            "- Use textbooks, documentation, and educational tutorials."
        )