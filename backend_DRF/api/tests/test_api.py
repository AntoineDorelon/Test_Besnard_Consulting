import pytest, json
from rest_framework import status

pytestmark = pytest.mark.django_db
values_url = "http://127.0.0.1/api/values/"
from api.models import AgileValues, AgilePrinciples

def test_zero_values_in_db_should_return_empty_list(client) -> None:
    response = client.get(values_url)
    assert response.status_code == 200
    assert response.json() == []

