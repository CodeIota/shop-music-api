from config_db import Session
from models.album_model import Album
from models.song_model import Song
from schemas.album_schema import AlbumInDB
from schemas.song_schema import SongInDB


class AlbumRepo:

    async def get_song_list_from_album(self, *, id: int, db: Session):
        album: AlbumInDB = db.query(Album).get(id)
        album.songs: list(SongInDB) = db.query(Song).join(Album).filter(Album.AlbumId == id).all()
        return album