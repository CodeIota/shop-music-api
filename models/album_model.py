from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config_db import Base
from models.song_model import Song 

class Album(Base):
    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))
    songs = relationship(Song, backref = 'albums')