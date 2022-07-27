from sqlalchemy import Column, Float, ForeignKey, Integer, String
from config_db import Base 
from sqlalchemy.orm import relationship

from models.genre_model import Genre
from models.media_type_model import MediaType

class Song(Base):
    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Composer = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeID'))
    mediaType = relationship(MediaType, backref="media_types")
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    genre = relationship(Genre, backref ='genres')


