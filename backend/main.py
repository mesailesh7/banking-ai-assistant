from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.auth import router as auth_router

setup_logging()

app = FastAPI(title=settings.APP_NAME)

app.include_router(health_router, prefix=settings.API_V1_PREFIX, tags=["Health"])
app.include_router(auth_router, prefix=settings.API_V1_PREFIX)
