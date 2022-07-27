from sqlalchemy import Column, Integer, String
from config_db import Base 


class Genre(Base): 
    __tablename__ = 'genres'
    GenreId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    