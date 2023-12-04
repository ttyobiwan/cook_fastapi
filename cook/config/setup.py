from fastapi import FastAPI
from ratelimit import RateLimitMiddleware, Rule, types
from ratelimit.backends.simple import MemoryBackend

from cook.api.urls import root_router
from cook.config.logs import logging_middleware, setup_logging
from cook.config.settings import settings


def init_logging(app: FastAPI) -> None:
    """Attach structlog into the app."""
    setup_logging(json_logs=not settings.debug, log_level="INFO")
    app.middleware("http")(logging_middleware)


def init_routes(app: FastAPI) -> None:
    """Attach routes into the app."""
    app.include_router(root_router)


def init_rate_limiter(app: FastAPI):
    """Limit the number of requests per second."""

    async def auth_func(scope: types.Scope) -> tuple[str, str]:
        """Recognize user by either the token or the IP address."""
        for header, value in scope["headers"]:
            if header == "authorization":
                return value, "default"
        return scope["client"], "default"

    app.add_middleware(
        RateLimitMiddleware,
        authenticate=auth_func,
        backend=MemoryBackend(),
        config={
            # 'RATE_LIMIT' requests per second
            r"^/*": [Rule(second=settings.rate_limit, group="default")],
        },
    )


def setup_app(app: FastAPI) -> FastAPI:
    """Set up the app before starting."""
    init_logging(app)
    init_routes(app)
    init_rate_limiter(app)
    return app
