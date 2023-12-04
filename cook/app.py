from fastapi import FastAPI

from cook.config.settings import settings


def create_app() -> FastAPI:
    """Create a new app and attach routes."""
    return FastAPI(
        title="Cook",
        debug=settings.debug,
        docs_url=f"{settings.api_prefix}/api/docs",
        openapi_url=f"{settings.api_prefix}/api/openapi.json",
    )
