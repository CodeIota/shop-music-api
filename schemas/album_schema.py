from typing import Optional
from pydantic import BaseModel

class AlbumModel(BaseModel):
    Title: Optional[str]

class AlbumInDB(AlbumModel):
    Title: str

    class Config:
        orm_mode = True