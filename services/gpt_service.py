import openai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def generate_questions(topic: str, difficulty: str):
    """
    Generate multiple-choice questions using GPT.

    Args:
        topic (str): The topic for the questions.
        difficulty (str): The difficulty level (easy, medium, hard).

    Returns:
        list: A list of questions with answers and explanations.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant that generates multiple-choice questions. "
                "Your responses must be in JSON format with the following structure: "
                "[{"
                '"question": "The question text", '
                '"options": ["Option A", "Option B", "Option C", "Option D"], '
                '"answer": "Correct Answer", '
                '"explanation": "Explanation for the correct answer"'
                "}]."
            )
        },
        {
            "role": "user",
            "content": (
                f"Generate 20 multiple-choice questions on the topic '{topic}' "
                f"with difficulty '{difficulty}'. Each question must have 4 options, "
                "one correct answer, and an explanation for the correct answer."
            )
        },
    ]

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
        )
        questions = response.choices[0].message.content
        return questions
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Failed to generate questions"}