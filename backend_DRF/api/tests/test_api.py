import pytest
import json
from rest_framework import status
from api.models import AgileValues, AgilePrinciples

pytestmark = pytest.mark.django_db
values_url = "http://127.0.0.1/api/values/"

@pytest.fixture
def example_single_value_in_db() -> AgileValues:
    test_value = AgileValues.objects.create(title='Flexibility')
    return test_value

@pytest.fixture
def example_four_values_in_db() -> None:
    AgileValues.objects.bulk_create([
        AgileValues(title='Flexibility'),
        AgileValues(title='Competitiveness'),
        AgileValues(title='Documentation'),
        AgileValues(title='Responsiveness')
    ])
    pass

def test_zero_values_in_db_should_return_empty_list(client) -> None:
    response = client.get(values_url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_one_value_should_succeed(client, example_single_value_in_db) -> None:
    response = client.get(values_url)
    response_content = response.json()[0]
    assert response.status_code == status.HTTP_200_OK
    assert response_content.get('title') == example_single_value_in_db.title


def test_modify_a_value_should_succeed(client, example_single_value_in_db) -> None:
    response = client.put(path=f'http://127.0.0.1:8000/api/values/{example_single_value_in_db.id}/',
                          data={'title': 'New value'},
                          content_type='application/json')
    assert response.status_code == 200
    assert response.content == b'{"id":1,"title":"New value"}'
    example_single_value_in_db.refresh_from_db()
    assert example_single_value_in_db.title == 'New value'


def test_delete_a_value_should_succeed(client, example_four_values_in_db) -> None:
    response = client.get(values_url)
    assert response.status_code == status.HTTP_200_OK
    assert AgileValues.objects.all().count() == 4
    response = client.delete(path="http://127.0.0.1:8000/api/values/3/")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert AgileValues.objects.all().count() == 3


def test_try_create_a_fifth_value_should_fail(client, example_four_values_in_db) -> None:
    pass


