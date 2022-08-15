from fastapi import APIRouter

from app.api.api_v1.endpoints import announcement

api_router = APIRouter()

api_router.include_router(announcement.router, prefix="/announcement", tags=["announcement"])
