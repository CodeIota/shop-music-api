from fastapi.testclient import TestClient

class TestGetSongsBySinger():
    def test_get_full_song_data(self, client: TestClient):
        res = client.get("/music-store/api/v1/song/900", headers={"accept": "application/json"})
        data = res.json()
        assert data == {
                "Name": "I Shot The Sheriff",
                "Milliseconds": 263862,
                "Bytes": 8738973,
                "UnitPrice": 0.99,
                "genre": {
                    "Name": "Blues"
                },
                "mediaType": {
                    "Name": "MPEG audio file"
                }
                }