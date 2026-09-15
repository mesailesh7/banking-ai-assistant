from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration.
    Values are loaded from .env
    """

    APP_NAME: str = "Banking AI Assistant"
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
