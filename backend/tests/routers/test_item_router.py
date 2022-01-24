from backend.models import item
from fastapi.testclient import TestClient
from tests.utils import utils


def test_create_item(client: TestClient):
    itemname = utils.random_string()
    price = utils.random_float()
    response = client.post(
        "/items",
        json={"itemname": itemname, "price": price},
    )
    assert response.status_code == 200
    res_data = response.json()
    assert res_data["itemname"] == itemname
    assert res_data["price"] == price
    assert "id" in res_data
    id = res_data["id"]

    response = client.get(f"/items/{id}")
    assert response.status_code == 200
    res_data = response.json()
    assert res_data["itemname"] == itemname
    assert res_data["price"] == price
    assert res_data["id"] == id
