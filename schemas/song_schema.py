from email.policy import strict
from typing import Optional
from pydantic import BaseModel

class SongModel(BaseModel):
    Name: Optional[str]

class SongInDB(SongModel):
    Name: str
    Composer: str
    # Genre: str

    class Config:
        orm_mode = True

class FullSongData(SongModel):
    Name: str
    Composer: str 
    # MediaType: str
    # Genre: str
    Milliseconds: int
    Bytes: int
    UnitPrice: float