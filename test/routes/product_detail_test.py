from fastapi.testclient import TestClient
from env import settings
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()
local_prefix = "/product_details/"

fake_summary = fake.name()
fake_summary_2 = fake.name()
fake_description = fake.name()
fake_icon = fake.name()


def test_func_product_details():
    response = client.post(
        settings.API_PREFIX+"/users/token",
        data={"username": "coroo.wicaksono@gmail.com",
              "password": "mysecretpass"},
    )

    assert response.status_code == 200, response.text
    session_data = response.json()
    assert session_data['token_type'] is not None
    assert session_data['access_token'] is not None

    # CREATE PRODUCT DETAIL
    headers = {"Authorization":
               f"{session_data['token_type']} {session_data['access_token']}"}
    response = client.post(
        settings.API_PREFIX+local_prefix,
        headers=headers,
        json={"summary": fake_summary,
              "description": fake_description,
              "icon": fake_icon},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['id'] is not None
    assert "id" in data
    product_detail_id = data["id"]

    # READ PRODUCT DETAILS
    response = client.get(settings.API_PREFIX+local_prefix,
                          headers=headers,)
    assert response.status_code == 200

    # READ PRODUCT DETAIL
    response = client.get(settings.API_PREFIX+local_prefix+str(data['id']),
                          headers=headers,)
    assert response.status_code == 200

    # UPDATE PRODUCT DETAIL
    response = client.put(
        f"{settings.API_PREFIX}{local_prefix}{product_detail_id}",
        json={"summary": fake_summary_2,
              "description": fake_description,
              "icon": fake_icon},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["summary"] != fake_summary
    assert data["summary"] == fake_summary_2

    # DELETE PRODUCT DETAIL
    response = client.delete(
        f"{settings.API_PREFIX}{local_prefix}",
        json={"id": product_detail_id},
    )
    assert response.status_code == 200

    # NEGATIVE TEST
    wrong_id = "just-wrong-uuid"  # just random id

    # UPDATE PRODUCT DETAIL
    response = client.put(
        f"{settings.API_PREFIX}{local_prefix}{wrong_id}",
        json={"summary": fake_summary_2,
              "description": fake_description,
              "icon": fake_icon},
    )
    assert response.status_code == 404, response.text

    # DELETE PRODUCT DETAIL
    response = client.delete(
        f"{settings.API_PREFIX}{local_prefix}",
        json={"id": wrong_id},
    )
    assert response.status_code == 404

    # READ NOT EXIST PRODUCT DETAIL
    response = client.get(
        f"{settings.API_PREFIX}{local_prefix}{product_detail_id}",
        headers=headers,)
    assert response.status_code == 404
