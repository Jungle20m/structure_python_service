from fastapi import APIRouter

from app.api.routes import cross_check_report


router = APIRouter()
router.include_router(cross_check_report.router, tags=["cross_check_report"], prefix="/crosscheck")