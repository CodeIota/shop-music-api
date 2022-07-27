from typing import List
from sqlalchemy.orm import Session
from models.album_model import Album

from models.singer_model import Singer
from models.song_model import Song
from schemas.album_schema import AlbumInDB
from schemas.singer_schema import SingerInDB, SingerWithAlbums, SingerWithSongs
from schemas.song_schema import SongInDB

class SingerRepo:
    def get_all_singers(self, db: Session) -> List[SingerInDB]:
        singers: List[SingerInDB] = db.query(Singer).all()
        return singers
    
    def get_albums_by_singer(self, *, id: int, db: Session) -> SingerWithAlbums:
        singer: SingerWithAlbums = db.query(Singer).get(id)
        singer.albums: list[AlbumInDB] = db.query(Album).join(Singer).filter(Singer.ArtistId == id).all()
        # singer: AlbumInDB = db.query(Album).join(Singer).filter(Singer.ArtistId == id).all()
        # print(singer)
        return singer

    def get_songs_by_singer(self, *, id: int, db: Session) -> SingerWithSongs:
        singer: SingerWithSongs = db.query(Singer).get(id)
        singer.songs: list[SongInDB] = db.query(Song).join(Album).join(Singer).\
        filter(Singer.ArtistId == id).all()
        return singer
        