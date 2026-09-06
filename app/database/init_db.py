from app.database.connection import Base, engine
from app.database.models import CodeSubmission, ReviewReport
from app.database.coding_standard_model import CodingStandard   
from sqlalchemy import text


with engine.begin() as conn:
    conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
    Base.metadata.create_all(bind=conn)
    