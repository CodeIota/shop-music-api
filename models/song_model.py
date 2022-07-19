from sqlalchemy import Column, ForeignKey, Integer, String
from config_db import Base 

class Song(Base):
    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Composer = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))