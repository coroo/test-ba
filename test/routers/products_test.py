from fastapi.testclient import TestClient
from env import settings
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()
local_prefix = "/products/"

fake_slug = fake.name()
fake_slug_2 = fake.name()
fake_name = fake.name()
fake_premium_type = 'rate by age'


def test_func_products():
    response = client.post(
        settings.API_PREFIX+"/users/token",
        data={"username": "coroo.wicaksono@gmail.com",
              "password": "mysecretpass"},
    )

    assert response.status_code == 200, response.text
    session_data = response.json()
    assert session_data['token_type'] is not None
    assert session_data['access_token'] is not None

    # CREATE PRODUCT
    headers = {"Authorization":
               f"{session_data['token_type']} {session_data['access_token']}"}
    response = client.post(
        settings.API_PREFIX+local_prefix,
        headers=headers,
        json={"slug": fake_slug,
              "name": fake_name,
              "premium_type": fake_premium_type},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['id'] is not None
    assert "id" in data
    product_id = data["id"]

    # READ PRODUCTS
    response = client.get(settings.API_PREFIX+local_prefix,
                          headers=headers,)
    assert response.status_code == 200

    # READ PRODUCT
    response = client.get(settings.API_PREFIX+local_prefix+str(data['id']),
                          headers=headers,)
    assert response.status_code == 200

    # UPDATE PRODUCT
    response = client.put(
        f"{settings.API_PREFIX}{local_prefix}{product_id}",
        json={"slug": fake_slug_2,
              "name": fake_name,
              "premium_type": fake_premium_type},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["slug"] != fake_slug
    assert data["slug"] == fake_slug_2

    # DELETE PRODUCT
    response = client.delete(
        f"{settings.API_PREFIX}{local_prefix}",
        json={"id": product_id},
    )
    assert response.status_code == 200

    # NEGATIVE TEST
    wrong_id = "just-wrong-uuid"  # just random id

    # UPDATE PRODUCT
    response = client.put(
        f"{settings.API_PREFIX}{local_prefix}{wrong_id}",
        json={"slug": fake_slug_2,
              "name": fake_name,
              "premium_type": fake_premium_type},
    )
    assert response.status_code == 404, response.text

    # DELETE PRODUCT
    response = client.delete(
        f"{settings.API_PREFIX}{local_prefix}",
        json={"id": wrong_id},
    )
    assert response.status_code == 404

    # READ NOT EXIST PRODUCT
    response = client.get(f"{settings.API_PREFIX}{local_prefix}{product_id}",
                          headers=headers,)
    assert response.status_code == 404
