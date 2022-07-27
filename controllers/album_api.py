from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config_db import get_db
from repositories.album_repository import AlbumRepo
from schemas.album_schema import AlbumsWithSongs
from schemas.song_schema import FullSongData

album_router = APIRouter()

@album_router.get('/album/{id}', response_model = AlbumsWithSongs, status_code=status.HTTP_200_OK)
def get_song_list_from_album(id: int, db: Session = Depends(get_db)): 
    album_repo = AlbumRepo()
    return album_repo.get_song_list_from_album(id = id, db = db)