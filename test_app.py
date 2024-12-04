from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_postdata_reverse():
    response = client.post("/postdata", data={"text": '1230003219___9'})
    assert response.status_code == 200
    assert response.json() == ['9___9123000321']
