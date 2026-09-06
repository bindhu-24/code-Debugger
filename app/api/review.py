from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.review_schema import ReviewRequest,ReviewResponse, CodeReviewReport
from app.services.review_service import create_review
from app.database.dependencies import get_db

router = APIRouter()


@router.post("/review",
             response_model=ReviewResponse)
def review_code(
    request: ReviewRequest,
    db: Session = Depends(get_db)
):
    if len(request.code) > 10000:
        raise HTTPException(
            status_code=400,
            detail="code too large. Maximum allowed length is 10,000 characters."
        )
    
    review_report = create_review(
        db=db,
        language=request.language,
        code=request.code,
        context=request.context or ""
    )

    return ReviewResponse(
        review_id=review_report.id,
        status="completed",
        review=CodeReviewReport(
            score=review_report.score,
            summary=review_report.summary,
            issues=review_report.issues
        )
    )