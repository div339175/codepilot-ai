from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    repository: str


class FileAnalysisRequest(BaseModel):
    repository: str
    file_path: str