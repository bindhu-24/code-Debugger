from sqlalchemy.orm import Session

from app.database.models import CodingStandard
from app.services.embedding_service import generate_embedding


def retrieve_standards(
    db: Session,
    code: str,
    top_k: int = 3
):
    query_embedding = generate_embedding(code)

    results = (
        db.query(CodingStandard)
        .order_by(
            CodingStandard.embedding.cosine_distance(
                query_embedding
            )
        )
        .limit(top_k)
        .all()
    )

    return results