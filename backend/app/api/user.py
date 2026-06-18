from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.user import UserCreate
from app.services.user_service import create_user
from app.models.user import User
from app.services.leetcode_services import get_profile

router = APIRouter()

@router.post("/users")
def add_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, payload.username)

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/leetcode/{username}")
def fetch_profile(username: str):
    return get_profile(username)