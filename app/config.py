from pydantic import BaseSettings


class Settings(BaseSettings):
    # App Information
    APP_NAME: str = 'Cat Facts API'
    APP_VERSION: str = "1.0.0"
    APP_PREFIX: str = "/api"
    APP_DESCRIPTION: str = """Service to get facts"""

    # Server configuration
    DEBUG: bool = "true"
    LOGGER_NAME: str = "uvicorn.error"
