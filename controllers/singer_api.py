from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from repositories.singer_repository import SingerRepo
# from schemas.album_schema import AlbumInDB

from schemas.singer_schema import SingerInDB, SingerWithAlbums, SingerWithSongs
from config_db import get_db

singer_router = APIRouter()

# Retorna todos los artistas
@singer_router.get('/singers', response_model = List[SingerInDB], status_code=status.HTTP_200_OK)
async def get_all_singers(db: Session = Depends(get_db)): 
    singers_repo = SingerRepo()
    return await singers_repo.get_all_singers(db=db)

#retorna lista de albumes de un artista en especifico

@singer_router.get('/singers/{id}', response_model= SingerWithAlbums, status_code=status.HTTP_200_OK)
async def get_albums_by_singer(id: int, db: Session = Depends(get_db)): 
    repo = SingerRepo()
    return await repo.get_albums_by_singer(id = id, db = db)

# retorna lista de canciones de un artista 
@singer_router.get('/singer/{id}', response_model= SingerWithSongs, status_code=status.HTTP_200_OK)
async def get_songs_by_singer(id: int, db: Session = Depends(get_db)): 
    repo = SingerRepo()
    return await repo.get_songs_by_singer(id = id, db = db)