from sqlalchemy import Column, Integer, String, Text
from database import Base

# Feedback table
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    message = Column(Text)

# No other tables needed since frontend is static
