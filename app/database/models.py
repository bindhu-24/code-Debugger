from sqlalchemy import Column, ForeignKey, String, Text, Integer, JSON
from app.database.connection import Base
from sqlalchemy.orm import Mapped, mapped_column ,relationship
from pgvector.sqlalchemy import Vector

class CodeSubmission(Base):
    __tablename__ = "code_submissions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    language: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    code: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    context: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )
    review_report = relationship(
        "ReviewReport", 
        back_populates="submission", 
        uselist=False
    )


class ReviewReport(Base):
    __tablename__ = "review_reports"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    submission_id: Mapped[int] = mapped_column(
        ForeignKey("code_submissions.id"),
        nullable=False
    )

    score: Mapped[int] = mapped_column(
        nullable=False
    )

    summary: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    issues: Mapped[list] = mapped_column(
        JSON,
        nullable=False
    )

    submission = relationship(
        "CodeSubmission",
        back_populates="review_report"
    )

class CodingStandard(Base):
    __tablename__ = "coding_standards"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    language: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(1536),
        nullable=True
    )