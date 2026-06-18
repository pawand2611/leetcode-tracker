from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from app.core.config import DATABASE_URL

from app.models.base import Base
from app.models.user import User

engine = create_engine(DATABASE_URL)
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done")


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)