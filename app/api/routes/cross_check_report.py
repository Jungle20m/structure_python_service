from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from starlette.responses import JSONResponse

from app.models.domain.cross_check_report import CrossCheckReport


router = APIRouter()
@router.post("")
def get_report(cross_check_data: CrossCheckReport) -> JSONResponse: 
    
    return JSONResponse({"status": "success"}, status_code=HTTP_200_OK)