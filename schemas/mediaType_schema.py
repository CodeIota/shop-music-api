from typing import Optional
from pydantic import BaseModel


class MediaTypeModel(BaseModel):
    Name: Optional[str]

class MediaTypeInDB(MediaTypeModel):
    Name: str

    class Config:
        orm_mode = True