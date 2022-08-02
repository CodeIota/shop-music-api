from fastapi import FastAPI, status
from fastapi.testclient import TestClient


class TestSingerRoute:
    def test_route_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.post(app.url_path_for('singer/'), {})
        assert res.status_code != status.HTTP_404_NOT_FOUND
