from fastapi import APIRouter

from cook.apps.internal.routes import router as internal_router
from cook.config.settings import settings

root_router = APIRouter(prefix=settings.api_prefix)

api_router = APIRouter(prefix="/api")

api_router.include_router(internal_router)

root_router.include_router(api_router)
