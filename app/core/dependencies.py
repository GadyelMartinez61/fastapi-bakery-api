from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import decode_access_token
from app.repositories.user_repo import UserRepo

security = HTTPBearer(auto_error=False)


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials is None:
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload = decode_access_token(credentials.credentials)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    username = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid payload")

    user = UserRepo().get(username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
