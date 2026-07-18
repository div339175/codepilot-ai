from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    repository: str