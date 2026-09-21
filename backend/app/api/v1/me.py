from fastapi import Depends
from app.core.dependencies import get_current_user

from fastapi import FastAPI

router = FastAPI()

@router.get('/me')
async def me(
        user = Depends(get_current_user),
):
    return user