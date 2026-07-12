from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.review_schema import ReviewRequest
from app.services.review_service import create_review
from app.database.dependencies import get_db

router = APIRouter()


@router.post("/review")
def review_code(
    request: ReviewRequest,
    db: Session = Depends(get_db)
):
    review = create_review(
        db=db,
        language=request.language,
        code=request.code,
        context=request.context or ""
    )

    return {
    "review_id": review.id,
    "status": "completed",
    "review": {
        "score": review.score,
        "summary": review.summary,
        "issues": review.issues
    }
}