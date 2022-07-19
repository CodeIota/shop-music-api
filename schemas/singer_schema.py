from typing import Optional
from pydantic import BaseModel

from schemas.album_schema import AlbumInDB
from schemas.song_schema import SongInDB

class SingerModel(BaseModel):
    Name: Optional[str]
    # albums: Optional[list[AlbumInDB]]
    # songs: Optional[list[]]
    

class SingerInDB(SingerModel): 
    Name: str

    class Config:
        orm_mode = True

class SingerWithAlbums(SingerModel):
    Name: str
    albums: list[AlbumInDB]

    class Config:
        orm_mode = True

class SingerWithSongs(SingerModel):
    Name: str
    songs: list[SongInDB]

    class Config:
        orm_mode = True
    