from typing import Optional
from pydantic import BaseModel


class GenreModel(BaseModel):
    Name: Optional[str]

class GenreInDB(GenreModel):
    Name: str

    class Config:
        orm_mode = True