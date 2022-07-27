from typing import List, Optional
from pydantic import BaseModel

from schemas.genre_schema import GenreInDB
from schemas.mediaType_schema import MediaTypeInDB

class SongModel(BaseModel):
    Name: Optional[str]

class SongInDB(SongModel):
    Name: str
    # Composer: str
    # Genre: str

    class Config:
        orm_mode = True

class FullSongData(SongModel):
    Name: str
    # Composer: str 
    Milliseconds: int
    Bytes: int
    UnitPrice: float
    genre: GenreInDB
    mediaType: MediaTypeInDB
    class Config:
        orm_mode = True
