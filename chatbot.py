import json
import os

# Load knowledge base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_FILE = os.path.join(BASE_DIR, "chatbot_knowledge.json")

with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
    knowledge = json.load(f)


def chatbot_response(user_message: str):
    """
    Returns an answer based on keywords found in the knowledge base.
    If no keyword matches, returns a default message.
    """
    msg = user_message.lower()

    # Search for keywords
    for key, answer in knowledge.items():
        if key.lower() in msg:
            return answer

    return (
        "I can help you understand neurological conditions like Alzheimer's, Parkinson's, "
        "and general brain health. Please ask a question related to the site content."
    )
