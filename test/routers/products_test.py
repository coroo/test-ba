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


def test_func_create_relationship_mockup_products():
    response = client.post(
        settings.API_PREFIX+"/users/token",
        data={"username": "coroo.wicaksono@gmail.com",
              "password": "mysecretpass"},
    )

    assert response.status_code == 200, response.text
    session_data = response.json()
    assert session_data['token_type'] is not None
    assert session_data['access_token'] is not None

    # CREATE PRODUCT CATEGORY
    headers = {"Authorization":
               f"{session_data['token_type']} {session_data['access_token']}"}
    response = client.post(
        settings.API_PREFIX+"/product_categories/",
        headers=headers,
        json={"name": fake_name},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['id'] is not None
    assert "id" in data

    # CREATE PRODUCT DETAIL
    headers = {"Authorization":
               f"{session_data['token_type']} {session_data['access_token']}"}
    response = client.post(
        settings.API_PREFIX+"/product_details/",
        headers=headers,
        json={"summary": fake_name,
              "description": fake_name,
              "icon": fake_name},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['id'] is not None
    assert "id" in data

    # CREATE PRODUCT INSURANCE TYPE
    headers = {"Authorization":
               f"{session_data['token_type']} {session_data['access_token']}"}
    response = client.post(
        settings.API_PREFIX+"/product_insurance_types/",
        headers=headers,
        json={"name": fake_name},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['id'] is not None
    assert "id" in data


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

    # READ FIRST PRODUCT CATEGORY
    response = client.get(settings.API_PREFIX+"/product_categories/")
    assert response.status_code == 200, response.text
    category_data = response.json()
    assert category_data[0]["id"] is not None
    category_id = category_data[0]["id"]

    # READ FIRST PRODUCT DETAIL
    response = client.get(settings.API_PREFIX+"/product_details/")
    assert response.status_code == 200, response.text
    detail_data = response.json()
    assert detail_data[0]["id"] is not None
    detail_id = detail_data[0]["id"]

    # READ FIRST PRODUCT INSURANCE TYPE
    response = client.get(settings.API_PREFIX+"/product_insurance_types/")
    assert response.status_code == 200, response.text
    insurance_type_data = response.json()
    assert insurance_type_data[0]["id"] is not None
    insurance_type_id = insurance_type_data[0]["id"]

    # CREATE PRODUCT
    headers = {"Authorization":
               f"{session_data['token_type']} {session_data['access_token']}"}
    response = client.post(
        settings.API_PREFIX+local_prefix,
        headers=headers,
        json={"slug": fake_slug,
              "name": fake_name,
              "category_id": category_id,
              "insurance_type_id": insurance_type_id,
              "detail_id": detail_id,
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
              "category_id": category_id,
              "insurance_type_id": insurance_type_id,
              "detail_id": detail_id,
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
              "category_id": category_id,
              "insurance_type_id": insurance_type_id,
              "detail_id": detail_id,
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


def test_func_delete_relationship_mockup_products():
    response = client.post(
        settings.API_PREFIX+"/users/token",
        data={"username": "coroo.wicaksono@gmail.com",
              "password": "mysecretpass"},
    )

    assert response.status_code == 200, response.text
    session_data = response.json()
    assert session_data['token_type'] is not None
    assert session_data['access_token'] is not None

    # READ FIRST PRODUCT CATEGORY
    response = client.get(settings.API_PREFIX+"/product_categories/")
    assert response.status_code == 200, response.text
    category_data = response.json()
    assert category_data[0]["id"] is not None
    category_id = category_data[0]["id"]

    # READ FIRST PRODUCT DETAIL
    response = client.get(settings.API_PREFIX+"/product_details/")
    assert response.status_code == 200, response.text
    detail_data = response.json()
    assert detail_data[0]["id"] is not None
    detail_id = detail_data[0]["id"]

    # READ FIRST PRODUCT INSURANCE TYPE
    response = client.get(settings.API_PREFIX+"/product_insurance_types/")
    assert response.status_code == 200, response.text
    insurance_type_data = response.json()
    assert insurance_type_data[0]["id"] is not None
    insurance_type_id = insurance_type_data[0]["id"]

    # DELETE PRODUCT CATEGORY
    response = client.delete(
        f"{settings.API_PREFIX}/product_categories/",
        json={"id": category_id},
    )
    assert response.status_code == 200

    # DELETE PRODUCT DETAIL
    response = client.delete(
        f"{settings.API_PREFIX}/product_details/",
        json={"id": detail_id},
    )
    assert response.status_code == 200

    # DELETE PRODUCT INSURANCE TYPE
    response = client.delete(
        f"{settings.API_PREFIX}/product_insurance_types/",
        json={"id": insurance_type_id},
    )
    assert response.status_code == 200
