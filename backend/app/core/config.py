from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration.
    Values are loaded from .env
    """

    APP_NAME: str = "Banking AI Assistant"
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = "development"
    # LOG_LEVEL: str = "INFO"

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"


settings = Settings()
