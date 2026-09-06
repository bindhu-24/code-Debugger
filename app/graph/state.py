from typing import TypedDict
from sqlalchemy.orm import Session

class ReviewState(TypedDict, total=False):
    submission_id: int

    db: Session
    
    language: str
    code: str
    context: str

    analysis: str
    retrieved_standards: list

    review_result: dict
    review: str

    issues_found: bool

    review_report_id: int
    