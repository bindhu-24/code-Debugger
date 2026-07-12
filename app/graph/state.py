from typing import TypedDict
from sqlalchemy.orm import Session

class ReviewState(TypedDict):
    db: Session
    language: str
    code: str
    context: str
    standards: str
    review_result: dict
    # review_id: int
    submission_id: int
    saved_review: object