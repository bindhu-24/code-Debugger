from sqlalchemy import Column, ForeignKey, String, Text, Integer, JSON
from app.database.connection import Base
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector

class CodeSubmission(Base):
    __tablename__ = "code_submissions"

    id = Column(Integer, primary_key=True, index=True)
    language = Column(String)
    code = Column(Text)
    context = Column(Text)
    review = relationship(
        "ReviewReport", 
        back_populates="submission", 
        uselist=False
    )


class ReviewReport(Base):
    __tablename__ = "review_reports"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(
        Integer, 
        ForeignKey("code_submissions.id")
        )
    score = Column(Integer)
    summary = Column(Text)
    issues = Column(JSON)

    submission = relationship("CodeSubmission", back_populates="review")

class CodingStandard(Base):
    __tablename__ = "coding_standards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category = Column(String)
    content = Column(Text)
    embedding = Column(Vector(1536))