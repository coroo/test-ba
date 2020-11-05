from fastapi.testclient import TestClient
from env import settings
from faker import Faker
import pytest

from main import app

from test.routes.product_category_test import TestProductCategories
from test.routes.product_detail_test import TestProductDetails
from test.routes.product_insurance_type_test import TestProductInsuranceTypes

client = TestClient(app)
fake = Faker()
local_prefix = "/products/"

fake_slug = fake.name()
fake_slug_2 = fake.name()
fake_name = fake.name()
fake_premium_type = 'rate by age'


class TestProducts():
    @pytest.fixture(autouse=True)
    def _setup(self):
        # REQUEST AND TOKEN SETUP
        response = client.post(
            settings.API_PREFIX+"/users/token",
            data={"username": "coroo.wicaksono@gmail.com",
                  "password": "mysecretpass"},
        )

        assert response.status_code == 200, response.text
        session_data = response.json()
        assert session_data['token_type'] is not None
        assert session_data['access_token'] is not None

        # TOKEN HEADERS
        headers = {
            "Authorization":
            f"{session_data['token_type']} {session_data['access_token']}"}
        self.headers = headers

        # READ FIRST PRODUCT CATEGORY
        TestProductCategories.test_create(self)
        response = client.get(settings.API_PREFIX+"/product_categories/")
        assert response.status_code == 200, response.text
        category_data = response.json()
        assert category_data[0]["id"] is not None
        self.category_id = category_data[0]["id"]

        # READ FIRST PRODUCT DETAIL
        TestProductDetails.test_create(self)
        response = client.get(settings.API_PREFIX+"/product_details/")
        assert response.status_code == 200, response.text
        detail_data = response.json()
        assert detail_data[0]["id"] is not None
        self.detail_id = detail_data[0]["id"]

        # READ FIRST PRODUCT INSURANCE TYPE
        TestProductInsuranceTypes.test_create(self)
        response = client.get(settings.API_PREFIX+"/product_insurance_types/")
        assert response.status_code == 200, response.text
        insurance_type_data = response.json()
        assert insurance_type_data[0]["id"] is not None
        self.insurance_type_id = insurance_type_data[0]["id"]

        # NEGATIVE TEST
        self.wrong_id = 912093018209302910

    def test_create(self):
        response = client.post(
            settings.API_PREFIX+local_prefix,
            headers=self.headers,
            json={"slug": fake_slug,
                  "name": fake_name,
                  "category_id": self.category_id,
                  "insurance_type_id": self.insurance_type_id,
                  "detail_id": self.detail_id,
                  "premium_type": fake_premium_type},
        )
        assert response.status_code == 200, response.text

    # def test_get(self):
    #     # PREPARATION GET ID
    #     response = client.get(
    #         settings.API_PREFIX+local_prefix,
    #         headers=self.headers,
    #     )
    #     assert response.status_code == 200, response.text
    #     data = response.json()
    #     assert data[0]['id'] is not None
    #     assert "id" in data[0]
    #     self.id_test = data[0]['id']

    #     response = client.get(settings.API_PREFIX+local_prefix,
    #                           headers=self.headers,)
    #     assert response.status_code == 200

    #     response = client.get(
    #         settings.API_PREFIX+local_prefix+str(data[0]['id']),
    #         headers=self.headers,)
    #     assert response.status_code == 200

    # def test_update(self):
    #     # PREPARATION GET ID
    #     response = client.get(
    #         settings.API_PREFIX+local_prefix,
    #         headers=self.headers,
    #     )
    #     assert response.status_code == 200, response.text
    #     data = response.json()
    #     assert data[0]['id'] is not None
    #     assert "id" in data[0]
    #     self.id_test = data[0]['id']

    #     response = client.get(settings.API_PREFIX+local_prefix,
    #                           headers=self.headers,)
    #     assert response.status_code == 200

    #     response = client.put(
    #         f"{settings.API_PREFIX}{local_prefix}{self.id_test}",
    #         json={"slug": fake_slug_2,
    #               "name": fake_name,
    #               "category_id": self.category_id,
    #               "insurance_type_id": self.insurance_type_id,
    #               "detail_id": self.detail_id,
    #               "premium_type": fake_premium_type},
    #     )
    #     assert response.status_code == 200, response.text
    #     data = response.json()
    #     assert data["slug"] != fake_slug
    #     assert data["slug"] == fake_slug_2

    # def test_delete(self):
    #     # PREPARATION GET ID
    #     response = client.get(
    #         settings.API_PREFIX+local_prefix,
    #         headers=self.headers,
    #     )
    #     assert response.status_code == 200, response.text
    #     data = response.json()
    #     assert data[0]['id'] is not None
    #     assert "id" in data[0]
    #     self.id_test = data[0]['id']

    #     response = client.get(settings.API_PREFIX+local_prefix,
    #                           headers=self.headers,)
    #     assert response.status_code == 200

    #     response = client.delete(
    #         f"{settings.API_PREFIX}{local_prefix}",
    #         json={"id": self.id_test},
    #     )
    #     assert response.status_code == 200

    # # ============ NEGATIVE TEST ============
    # def test_negative_get(self):
    #     response = client.get(f"{settings.API_PREFIX}{local_prefix}" +
    #                           f"{self.wrong_id}",
    #                           headers=self.headers,)
    #     assert response.status_code == 404

    # def test_negative_update(self):
    #     response = client.put(
    #         f"{settings.API_PREFIX}{local_prefix}{self.wrong_id}",
    #         json={"slug": fake_slug_2,
    #               "name": fake_name,
    #               "category_id": self.category_id,
    #               "insurance_type_id": self.insurance_type_id,
    #               "detail_id": self.detail_id,
    #               "premium_type": fake_premium_type},
    #     )
    #     assert response.status_code == 404, response.text

    # def test_negative_delete(self):
    #     response = client.delete(
    #         f"{settings.API_PREFIX}{local_prefix}",
    #         json={"id": self.wrong_id},
    #     )
    #     assert response.status_code == 404
