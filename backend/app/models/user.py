from sqlalchemy import Column, Integer, String
from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    ranking = Column(Integer)
    rating = Column(Integer)
    real_name = Column(String)
    avatar = Column(String)
    
    easy_solved = Column(Integer)
    medium_solved = Column(Integer)
    hard_solved = Column(Integer)
    total_solved = Column(Integer)