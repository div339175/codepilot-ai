from pydantic import BaseModel

class DashboardResponse(BaseModel):

    total_repositories: int

    analyzed_repositories: int

    total_languages: int

    total_frameworks: int

    repositories: list