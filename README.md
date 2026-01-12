NeuroCare Backend
Backend API for NeuroCare, providing AI-powered neurological support and user feedback management.

Features
Chatbot API – AI assistant for users.


Feedback API – Collect and store user feedback.


Database integration – SQLite for local storage.


Built with FastAPI for fast and robust endpoints.



Tech Stack
Python 3.11+


FastAPI


Uvicorn


SQLAlchemy


SQLite



Setup
Clone the repo


git clone https://github.com/YOUR_USERNAME/neurocare-backend.git
cd neurocare-backend

Create & activate a virtual environment


python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies


pip install -r requirements.txt

Set environment variables in .env:


DATABASE_URL=sqlite:///neurocare.db
CHATBOT_KNOWLEDGE=chatbot_knowledge.json


API Endpoints
Chatbot
POST /chat – Send a message to the AI.


Request body: { "message": "Hello" }


Response body: { "response": "Hi! How can I help?", "sentiment": "positive", "emotion": "happy" }


Feedback
POST /feedback – Submit user feedback.


Request body: { "name": "...", "email": "...", "rating": 5, "message": "..." }


Response body: { "success": true, "message": "Feedback submitted successfully." }



Run Server
uvicorn main:app --reload

Access API docs: http://127.0.0.1:8000/docs



Contributing
Fork → Feature branch → Commit → Pull request



