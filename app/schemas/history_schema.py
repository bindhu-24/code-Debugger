from pydantic import BaseModel
from typing import List, Dict, Any

class ReviewHistoryResponse(BaseModel):
    id: int
    submission_id: int
    score: int
    summary: str
    issues: List[Dict[str, Any]]

    class Config:
        from_attributes = True
