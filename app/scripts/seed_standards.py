from app.seed.coding_standards import STANDARDS
from app.database.connection import SessionLocal
from app.services.embedding_service import generate_embedding   
from app.database.models import CodingStandard

db = SessionLocal()

for item in STANDARDS:
    embedding = generate_embedding(item["content"])
    standard = CodingStandard(
        title=item["title"],
        category=item["category"],
        content=item["content"],
        embedding=embedding
    )
    db.add(standard)
db.commit()
print("Coding standards seeded successfully.")
