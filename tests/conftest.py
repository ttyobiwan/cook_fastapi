from typing import AsyncGenerator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient

from cook.app import create_app
from cook.config.settings import settings
from cook.config.setup import setup_app


@pytest.fixture()
def test_app() -> FastAPI:
    """Create app for testing."""
    app = create_app()
    return setup_app(app)


@pytest_asyncio.fixture()
async def client(test_app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Create http client."""
    async with AsyncClient(
        app=test_app,
        base_url=f"http://test.com{settings.api_prefix}",
    ) as client:
        yield client
