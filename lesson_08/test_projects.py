import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://ru.yougile.com/api-v2"
API_TOKEN = os.getenv("API_TOKEN")


def headers():
    return {"Authorization": f"Bearer {API_TOKEN}"}


def create_project(title):
    response = requests.post(
        f"{API_URL}/projects",
        headers=headers(),
        json={"title": title}
    )
    return response


def get_project(project_id):
    response = requests.get(
        f"{API_URL}/projects/{project_id}",
        headers=headers()
    )
    return response


def update_project(project_id, title):
    response = requests.put(
        f"{API_URL}/projects/{project_id}",
        headers=headers(),
        json={"title": title}
    )
    return response


def delete_project(project_id):
    requests.delete(
        f"{API_URL}/projects/{project_id}",
        headers=headers()
    )


# ---- POST /projects ----
def test_create_project_positive():
    response = create_project("Test Project")
    assert response.status_code == 201
    project_id = response.json()["id"]
    delete_project(project_id)


def test_create_project_negative():
    response = requests.post(
        f"{API_URL}/projects",
        headers=headers(),
        json={}
    )
    assert response.status_code == 400


# ---- GET /projects/{id} ----
def test_get_project_positive():
    create_response = create_project("Test Get Project")
    project_id = create_response.json()["id"]

    response = get_project(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Get Project"

    delete_project(project_id)


def test_get_project_negative():
    response = get_project("nonexistent-id-123")
    assert response.status_code == 404


# ---- PUT /projects/{id} ----
def test_update_project_positive():
    create_response = create_project("Old Title")
    project_id = create_response.json()["id"]

    response = update_project(project_id, "New Title")
    assert response.status_code == 200

    get_response = get_project(project_id)
    assert get_response.json()["title"] == "New Title"

    delete_project(project_id)


def test_update_project_negative():
    response = update_project("nonexistent-id-123", "New Title")
    assert response.status_code == 404
