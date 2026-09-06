from unittest.mock import Base
from sqlalchemy import engine

Base.metadata.create_all(bind=engine)