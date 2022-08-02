
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config_db import Base

DB_URL = 'sqlite:///./test.db'
engine = create_engine(DB_URL, connect_args ={'check_same_thread': False})

TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def testing_db():
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()