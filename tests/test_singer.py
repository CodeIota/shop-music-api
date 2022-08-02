from fastapi import FastAPI, status
from fastapi.testclient import TestClient

class TestSingerRoute:
    # check if the route (singers:get-all) is valid for access
    def test_get_all_route_exists(self, app: FastAPI, client: TestClient) -> None:
        res = client.post(app.url_path_for("singers:get-all"), {})
        assert res.status_code != status.HTTP_404_NOT_FOUND

class TestGetAll():
    def test_get_all_singers(self, app: FastAPI, client: TestClient):
        res = client.get(app.url_path_for("singers:get-all"), headers={"accept": "application/json"})
        data = res.json()
        assert data[1] == {'Name': "Accept"} # Should compare with "Accept" singer
        is_contained = {'Name': 'AC/DC'} in data # AC/DC should be in the data list
        assert is_contained == True     
        is_roselia_in = {'Name': 'Roselia'} not in data # should return True
        assert is_roselia_in == True
        assert res.status_code == status.HTTP_200_OK

class TestGetAlbumBySinger():
    def test_get_albums_by_singer_id(self, app: FastAPI, client: TestClient):
        res = client.get("/music-store/api/v1/singers/23", headers={"accept": "application/json"})
        data = res.json()
        assert data == {"Name": "Frank Zappa & Captain Beefheart", "albums": [{"Title": "Bongo Fury"}]}
        
class TestGetSongsBySinger():
    def test_get_songs_by_singer_id(self, app: FastAPI, client: TestClient):
        res = client.get("/music-store/api/v1/singer/30", headers={"accept": "application/json"})
        data = res.json()
        assert data == {"Name": "Jorge Vercilo","songs": []}


        