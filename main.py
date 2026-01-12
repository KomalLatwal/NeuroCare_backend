from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, Feedback
from schemas import FeedbackSchema, ChatRequest
from chatbot import chatbot_response

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="NeuroCare Backend")

# Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- HOME ----------
@app.get("/", summary="Check backend status")
def home():
    return {"message": "NeuroCare Backend Running Successfully"}


# ---------- FEEDBACK ----------
@app.post("/feedback", summary="Submit user feedback")
def submit_feedback(feedback: FeedbackSchema, db: Session = Depends(get_db)):
    fb = Feedback(
        name=feedback.name,
        email=feedback.email,
        message=feedback.message
    )
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return {"status": "saved", "feedback_id": fb.id}


@app.get("/feedback", summary="Get all feedback")
def get_feedback(db: Session = Depends(get_db)):
    return db.query(Feedback).order_by(Feedback.id.desc()).all()


# ---------- CHATBOT ----------
@app.post("/chat", summary="Ask chatbot a question")
def chat(request: ChatRequest):
    response = chatbot_response(request.message)
    return {"reply": response}
