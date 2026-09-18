from app.core.security import verify_password, create_access_token


class AuthService:

    async def login(self, user, password: str):
        if not verify_password(password, user.hashed_password):
            return None

        token = create_access_token(
            user.id,
            user.email
        )
        return token
