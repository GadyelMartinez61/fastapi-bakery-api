from app.core.security import hash_password, verify_password, create_access_token
from app.repositories.user_repo import UserRepo
from app.schemas.auth import UserResponse, TokenResponse
from fastapi import HTTPException


class AuthService:
    def register(
        self, username: str, password: str, role: str = "cashier"
    ) -> UserResponse:
        if UserRepo().get(username):
            raise HTTPException(status_code=400, detail="Username already exists")
        user = UserRepo().create(
            {
                "username": username,
                "password": hash_password(password),
                "role": role,
            }
        )
        return UserResponse(**user)

    def login(self, username: str, password: str) -> TokenResponse:
        user = UserRepo().get(username)
        if not user or not verify_password(password, user.get("password", "")):
            raise HTTPException(status_code=404, detail="Wrong username or password")
        token = create_access_token({"sub": username, "role": user["role"]})
        return TokenResponse(access_token=token)

    def get_profile(self, username: str) -> UserResponse:
        user = UserRepo().get(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(**user)
