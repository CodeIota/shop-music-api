from sqlalchemy import Column, Integer, String
from config_db import Base
from sqlalchemy.orm import relationship

from models.album_model import Album


class Singer(Base):
    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    albums = relationship(Album, backref ='artists')
