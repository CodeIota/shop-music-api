from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config_db import get_db
from repositories.song_repository import SongRepo
from schemas.song_schema import FullSongData

song_router = APIRouter()

@song_router.get('/song/{id}', response_model = FullSongData, status_code=status.HTTP_200_OK)
def get_full_song_data(id: int, db: Session = Depends(get_db)): 
    song_repo = SongRepo()

    song = song_repo.get_full_song_data(id = id, db = db)

    # if not song:
    #     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)

    return song