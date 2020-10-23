from fastapi.testclient import TestClient
from env import settings
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()
local_prefix = "/product_insurance_types/"

fake_name = fake.name()
fake_name_2 = fake.name()


def test_func_product_insurance_types():
    response = client.post(
        settings.API_PREFIX+"/users/token",
        data={"username": "coroo.wicaksono@gmail.com",
              "password": "mysecretpass"},
    )

    assert response.status_code == 200, response.text
    session_data = response.json()
    assert session_data['token_type'] is not None
    assert session_data['access_token'] is not None

    # CREATE PRODUCT INSURANCE TYPE
    headers = {"Authorization":
               f"{session_data['token_type']} {session_data['access_token']}"}
    response = client.post(
        settings.API_PREFIX+local_prefix,
        headers=headers,
        json={"name": fake_name},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['id'] is not None
    assert "id" in data
    product_insurance_type_id = data["id"]

    # READ PRODUCT INSURANCE TYPES
    response = client.get(settings.API_PREFIX+local_prefix,
                          headers=headers,)
    assert response.status_code == 200

    # READ PRODUCT INSURANCE TYPE
    response = client.get(settings.API_PREFIX+local_prefix+str(data['id']),
                          headers=headers,)
    assert response.status_code == 200

    # UPDATE PRODUCT INSURANCE TYPE
    response = client.put(
        f"{settings.API_PREFIX}{local_prefix}{product_insurance_type_id}",
        json={"name": fake_name_2},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] != fake_name
    assert data["name"] == fake_name_2

    # DELETE PRODUCT INSURANCE TYPE
    response = client.delete(
        f"{settings.API_PREFIX}{local_prefix}",
        json={"id": product_insurance_type_id},
    )
    assert response.status_code == 200

    # NEGATIVE TEST
    wrong_id = "just-wrong-uuid"  # just random id

    # UPDATE PRODUCT INSURANCE TYPE
    response = client.put(
        f"{settings.API_PREFIX}{local_prefix}{wrong_id}",
        json={"name": fake_name},
    )
    assert response.status_code == 404, response.text

    # DELETE PRODUCT INSURANCE TYPE
    response = client.delete(
        f"{settings.API_PREFIX}{local_prefix}",
        json={"id": wrong_id},
    )
    assert response.status_code == 404

    # READ NOT EXIST PRODUCT INSURANCE TYPE
    response = client.get(
        f"{settings.API_PREFIX}{local_prefix}{product_insurance_type_id}",
        headers=headers,)
    assert response.status_code == 404
