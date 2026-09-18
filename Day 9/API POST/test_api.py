from api_client import create_post, create_post_from_data

def test_create_post():
    response = create_post(
        "Python Practice",
        "Learning POST requests",
        1
    )

    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "Python Practice"
    assert data["body"] == "Learning POST requests"
    assert data["userId"] == 1

def test_created_post_has_id():
    response = create_post(
        "Second Post",
        "Testing generated ID",
        2
    )

    data = response.json()
    assert "id" in data

def test_create_post_from_data():
    post = {
        "title": "Automation",
        "body": "Learning API testing",
        "userId": 5
    }

    response = create_post_from_data(post)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == "Automation"
    assert data["body"] == "Learning API testing"
    assert data["userId"] == 5