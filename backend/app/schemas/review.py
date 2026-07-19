from pydantic import BaseModel


class ReviewRequest(BaseModel):
    repository: str


class ReviewResponse(BaseModel):

    repository: str

    bugs: list[str]

    security_issues: list[str]

    code_smells: list[str]

    performance_suggestions: list[str]

    best_practices: list[str]

    overall_score: float