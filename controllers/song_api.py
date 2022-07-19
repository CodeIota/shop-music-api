from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config_db import get_db
from schemas.song_schema import FullSongData

song_router = APIRouter()

@song_router.get('/song/{id}', response_model = List[FullSongData], status_code=status.HTTP_200_OK)
def get_full_song_data(db: Session = Depends(get_db)): 
    pass
    # singers_repo = SingerRepo()
    # return singers_repo.get_all_singers(db=db)