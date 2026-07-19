from fastapi import APIRouter

from app.dashboard.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

service = DashboardService()


@router.get("/overview")

def overview():

    return service.overview()