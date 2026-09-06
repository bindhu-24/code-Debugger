from pydantic import BaseModel, Field
from typing import Optional, List, Literal


class ReviewRequest(BaseModel):
    language: str
    code: str = Field(..., max_length=10000)
    context: Optional[str] = None


# class ReviewIssue(BaseModel):
#     severity: str
#     category: str
#     line_number: int
#     description: str
#     recommendation: str

class ReviewIssue(BaseModel):
    severity: Literal[
        "Low",
        "Medium",
        "High",
        "Critical"
    ]

    category: Literal[
        "Bug Risk",
        "Security",
        "Performance",
        "Readability",
        "Best Practice",
        "Code Smell"
    ]

    line_number: int
    description: str
    recommendation: str


class CodeReviewReport(BaseModel):
    score: int
    summary: str
    issues: List[ReviewIssue]

class ReviewResponse(BaseModel):
    review_id: int
    status: str
    review: CodeReviewReport