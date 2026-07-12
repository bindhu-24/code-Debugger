from app.database.connection import Base, engine

from app.database.models import CodeSubmission, ReviewReport

Base.metadata.create_all(bind=engine)   

print("Database tables created successfully.")