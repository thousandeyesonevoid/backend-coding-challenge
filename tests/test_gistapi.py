import pytest
from gistapi.gistapi import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.data == b"pong"


def test_search(client, mocker):
    gists = [
        {
            "id": "123456",
            "files": {"file1.py": {"content": "import lmno \n print('hello world')"}},
        }
    ]
    mocker.patch("github_service.fetch_all_gist_contents", return_value=gists)

    payload = {"username": "test_user", "pattern": "import lmno"}
    response = client.post("/api/v1/search", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["username"] == "test_user"
    assert data["pattern"] == "import lmno"
    assert data["matches"] == gists
