from flask import Blueprint, request, jsonify
from services.gpt_service import generate_questions

quiz_routes = Blueprint("quiz_routes", __name__)

@quiz_routes.route("/generate-questions", methods=["POST"])
def generate_questions_route():
    """
    Endpoint to generate multiple-choice questions based on user input.
    """
    data = request.json
    topic = data.get("topic")
    difficulty = data.get("difficulty", "medium")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    # Generate questions using GPT service
    questions = generate_questions(topic, difficulty)
    return jsonify(questions)
