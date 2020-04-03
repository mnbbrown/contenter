import pytest
from api.content.models import ContentType, Entity


def test_list_content_types(client):
    response = client.get("/admin/content/")
    assert response.status_code == 200


def test_create_content_type(client):
    response = client.post(
        "/admin/content/", json={"name": "content type", "fields": [{"name": "name", "type": "string"}]}
    )
    assert response.status_code == 200


def test_create_bad_content_type(client):
    response = client.post("/admin/content/", json={"fields": []})
    assert response.status_code == 400


def test_list_entities(client, db):
    content_type = ContentType("test", None, [{"name": "name", "type": "string"}])
    db.add(content_type)
    content_type_id = content_type.public_id
    db.flush()
    entity = Entity(content_type.id, {"name": "test"})
    db.add(entity)
    db.commit()
    response = client.get(f"/admin/content/{content_type_id}/entities")
    assert response.status_code == 200
    assert response.json()[0].get("name") == "test"
