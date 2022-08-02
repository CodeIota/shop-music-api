from fastapi import FastAPI
import pytest 

from fastapi.testclient import TestClient



@pytest.fixture
def app()-> FastAPI:
    from main import get_api
    return get_api()

def client(app: FastAPI) -> FastAPI:
    from config_test_db import testing_db
    from config_db import get_db
    app.dependency_overrides[get_db] = testing_db
    
    client = TestClient(app)
    return client
