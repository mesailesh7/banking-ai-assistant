from fastapi import FastAPI

router = FastAPI()


@router.get("/info")
async def get_info():
    """
    Application Info endpoint
    """
    return {"app_name": "Banking AI Assistant", "environment": "development"}
