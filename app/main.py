from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router
from app.api.errors.http_error import http_error_handler
from app.core.config import API_PREFIX, DATABASE_URL, PROJECT_NAME, VERSION


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, version=VERSION)
    # middleware
    application.add_middleware(
        CORSMiddleware,
    )
    # errors handler
    application.add_exception_handler(HTTPException, http_error_handler)
    # routes
    application.include_router(api_router, prefix=API_PREFIX)
    return application

app = get_application()