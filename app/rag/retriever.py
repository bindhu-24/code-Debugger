from sqlalchemy.orm import Session
from app.database.models import CodingStandard
from app.rag.embeddings import generate_embedding


def retrieve_standards(
    db: Session,
    query: str,
    language: str,
    category: str | None = None,
    limit: int = 5
):
    query_embedding = generate_embedding(query)

    query_db = (
        db.query(CodingStandard)
        .filter(CodingStandard.language == language)
    )

    if category:
        query_db = query_db.filter(
            CodingStandard.category == category
        )

    standards = (
        query_db
        .order_by(
            CodingStandard.embedding.cosine_distance(query_embedding)
        )
        .limit(limit)
        .all()
    )

    return standards