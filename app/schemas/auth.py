from pydantic import BaseModel, Field, ConfigDict
from enum import Enum

class Roles(str, Enum):
    ADMIN = "admin"
    CASHIER = "cashier"


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=100)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    username: str
    role: str
    is_active: bool

class RegisterRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=100)
    role: Roles = Field(Roles.CASHIER)
