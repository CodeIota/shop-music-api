from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.singer_api import singer_router
from controllers.album_api import album_router
from controllers.song_api import song_router
from config_db import Base, engine

def get_api():

    default_prefix = '/music-store/api/v1'
    Base.metadata.create_all(bind=engine)
    
    app = FastAPI(
        title='Music Shop API',
        description='Backend for Music Shop',
        version='0.1.0'
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    app.include_router(singer_router, prefix=default_prefix, tags=['Singers'])
    app.include_router(album_router, prefix=default_prefix, tags=['Albums'])
    app.include_router(song_router, prefix=default_prefix, tags=['Songs'])

    return app

app = get_api()
