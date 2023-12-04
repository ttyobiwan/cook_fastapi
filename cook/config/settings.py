from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings."""

    # App
    debug: bool = False

    # API
    api_prefix: str = "/cook"
    rate_limit: int = 100


settings = Settings()
