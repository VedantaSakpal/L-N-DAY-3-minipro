from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello DevOps Students!" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "UP"


def test_userDetails():
    client = app.test_client()
    response = client.get("/userDetails")

    assert response.status_code == 200
    assert respose.json["name"]=="Vedant"
    assert respose.json["age"]=="18"
    assert response.json["maritalStatus"] == "Married"

