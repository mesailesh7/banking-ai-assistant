from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Application health endpoint.
    """
    return {"status": "healthy", "service": "Banking AI Assistant", "version": "1.0.0"}
