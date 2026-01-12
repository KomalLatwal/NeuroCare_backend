from pydantic import BaseModel

# Feedback schema
class FeedbackSchema(BaseModel):
    name: str
    email: str
    message: str

# Chatbot request
class ChatRequest(BaseModel):
    message: str
