from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.user import UserCreate
from app.services.user_service import create_user, save_profile
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

@router.post("/users/fetch/{username}")
def fetch_user(
    username: str,
    db: Session = Depends(get_db)
):
    profile = get_profile(username)

    return save_profile(db, profile)