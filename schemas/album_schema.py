from typing import Optional
from pydantic import BaseModel

from schemas.song_schema import SongInDB

class AlbumModel(BaseModel):
    Title: Optional[str]

class AlbumInDB(AlbumModel):
    Title: str

    class Config:
        orm_mode = True

class AlbumsWithSongs(AlbumModel):
    Title: str
    songs: list[SongInDB]
    class Config:
        orm_mode = True