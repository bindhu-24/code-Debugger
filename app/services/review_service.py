from sqlalchemy.orm import Session

from app.graph.workflow import build_review_graph

from app.database.models import (
    CodeSubmission,
    ReviewReport,
)


def create_review(
    db: Session,
    language: str,
    code: str,
    context: str | None = None
):
    # --------------------------------------------------
    # 1. Save submitted code
    # --------------------------------------------------

    submission = CodeSubmission(
        language=language,
        code=code,
        context=context
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    print("Submission ID:", submission.id)

    # --------------------------------------------------
    # 2. Build LangGraph
    # ------------------------------------------------
    graph = build_review_graph()

    # --------------------------------------------------
    # 3. Execute LangGraph
    # -----------------------------------------------

    result = graph.invoke(
        {
            # "db": db,
            "submission_id": submission.id,
            "language": language,
            "code": code,
            "context": context or "",
        }
    )

    print("Graph Result:")
    print(result)

    # --------------------------------------------------
    # 4. Get saved reviewReport ID
    # --------------------------------------------------

    review_report_id = result.get("review_report_id")

    print("Review Report ID:", review_report_id)

    if not review_report_id:
        raise RuntimeError("Review report was not saved.")

    # --------------------------------------------------
    # 5. Get ReviewReport from database
    # --------------------------------------------------

    review_report = (db.query(ReviewReport).filter(
        ReviewReport.id == review_report_id
    ).first()
)
    if not review_report:
        raise RuntimeError(
            f"Review report {review_report_id} not found."
        )

    return review_report
