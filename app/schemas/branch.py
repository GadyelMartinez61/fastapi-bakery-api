from pydantic import BaseModel, Field, ConfigDict


class BranchCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(..., min_length=2, max_length=100)
    address: str = Field(..., min_length=2, max_length=200)
    phone_number: str = Field(..., min_length=11, max_length=15)
    is_active: bool = Field(True)


class BranchUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=100)
    address: str | None = Field(None, min_length=2, max_length=200)
    phone_number: str | None = Field(None, min_length=11, max_length=15)
    is_active: bool | None = None


class BranchResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # permite crear desde dict

    id: str
    name: str
    address: str
    phone_number: str
    is_active: bool
    created_at: str
    updated_at: str | None
