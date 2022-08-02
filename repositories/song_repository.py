from http.client import HTTPException
from config_db import Session
from models.genre_model import Genre
from models.media_type_model import MediaType
from models.song_model import Song
from schemas.genre_schema import GenreInDB
from schemas.song_schema import FullSongData
from fastapi import status


class SongRepo:
    async def get_full_song_data(self, *, id: int, db: Session) -> FullSongData:
        
        song: FullSongData = db.query(Song).get(id)
        song.genre: GenreInDB = db.query(Genre).join(Song).filter(Song.TrackId == id).first()
        song.mediaType = db.query(MediaType).join(Song).filter(Song.TrackId == id).first()

        return song