from fastapi.testclient import TestClient

class TestGetSongsBySinger():
    def test_get_albums_with_songs(self, client: TestClient):
        res = client.get("/music-store/api/v1/album/60", headers={"accept": "application/json"})
        data = res.json()
        assert data == {
  "Title": "Fireball",
  "songs": [
    {
      "Name": "Fireball"
    },
    {
      "Name": "No No No"
    },
    {
      "Name": "Strange Kind Of Woman"
    },
    {
      "Name": "Anyone's Daughter"
    },
    {
      "Name": "The Mule"
    },
    {
      "Name": "Fools"
    },
    {
      "Name": "No One Came"
    }
  ]
}