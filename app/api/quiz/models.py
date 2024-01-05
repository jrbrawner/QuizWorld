from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

from app.database import BaseModel

class Quiz(BaseModel, table=True):

    __tablename__ = "quiz"

    id: int = Field(primary_key=True, nullable=False)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    questions: list["Question"] = Relationship(back_populates="quiz")

class Question(BaseModel, table=True):

    __tablename__ = "question"
    id: int = Field(primary_key=True, nullable=False)
    question_text: str = Field()
    answer_text: str = Field()
    correct_answer: int = Field()
    quiz_id: int = Field(foreign_key="quiz.id")
    quiz: Quiz = Relationship(back_populates="questions")


