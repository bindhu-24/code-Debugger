from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List


from app.database.dependencies import get_db
from app.database.models import ReviewReport
from app.schemas.history_schema import ReviewHistoryResponse

router = APIRouter()

@router.get(
        "/reviews",
        response_model=List[ReviewHistoryResponse])
def get_reviews(
    db:Session = Depends(get_db)
):
    reviews = (
        db.query(ReviewReport)
        .order_by(ReviewReport.id.desc())
        .all()
    )
    return reviews
