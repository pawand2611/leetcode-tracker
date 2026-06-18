from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str

class UserResponse(BaseModel):
    id: int
    username: str
    ranking: int | None = None
    rating: int | None = None

    class Config:
        from_attributes = True