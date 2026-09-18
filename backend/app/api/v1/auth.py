from fastapi import APIRouter

from app.core.security import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse

router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)


@router.post('/login', response_model=TokenResponse)
async def login(payload: LoginRequest):
    # Todo: Test
    token = create_access_token(
        user_id=1,
        email=payload.email,
    )

    return TokenResponse(
        access_token=token,
    )
