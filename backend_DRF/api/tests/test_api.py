import pytest
from rest_framework import status
from api.models import AgileValues, AgilePrinciples

pytestmark = pytest.mark.django_db
values_url = "http://127.0.0.1:8000/api/values/"
principles_url = "http://127.0.0.1:8000/api/principles/"


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


@pytest.fixture
def example_single_principle_in_db() -> AgilePrinciples:
    test_principle = AgilePrinciples.objects.create(description='Customer satisfaction')
    return test_principle


@pytest.fixture
def example_twelve_principles_in_db() -> None:
    AgilePrinciples.objects.bulk_create([
        AgilePrinciples(description='Customer satisfaction'),
        AgilePrinciples(description='Accommodate changing'),
        AgilePrinciples(description='Frequent delivery '),
        AgilePrinciples(description='Collaboration between the business stakeholders and developers'),
        AgilePrinciples(description='Support, trust, and motivate the people involved'),
        AgilePrinciples(description='Enable face-to-face interactions'),
        AgilePrinciples(description='Working software is the primary measure of progress'),
        AgilePrinciples(description='Agile processes to support a consistent development pace'),
        AgilePrinciples(description='Attention to technical detail and design enhances agility'),
        AgilePrinciples(description='Simplicity'),
        AgilePrinciples(description='Self-organizing teams'),
        AgilePrinciples(description='Regular reflections on how to become more effective')
    ])
    pass


class TestValuesAPI:
    def test_zero_values_in_db_should_return_empty_list(self, client) -> None:
        response = client.get(values_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_retrieve_one_value_should_succeed(self, client, example_single_value_in_db) -> None:
        response = client.get(values_url)
        response_content = response.json()[0]
        assert response.status_code == status.HTTP_200_OK
        assert response_content.get('title') == example_single_value_in_db.title

    def test_modify_a_value_should_succeed(self, client, example_single_value_in_db) -> None:
        response = client.put(
            path=values_url+str(example_single_value_in_db.id)+'/',
            data={'title': 'New value'},
            content_type='application/json'
        )
        response_content = response.json()
        assert response.status_code == 200
        assert response_content.get('title') == 'New value'
        example_single_value_in_db.refresh_from_db()
        assert example_single_value_in_db.title == 'New value'

    def test_delete_a_value_should_succeed(self, client, example_four_values_in_db) -> None:
        response = client.get(values_url)
        assert response.status_code == status.HTTP_200_OK
        assert AgileValues.objects.all().count() == 4
        response = client.delete(path=values_url+'3/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert AgileValues.objects.all().count() == 3

    def test_try_create_a_fifth_value_should_fail(self, client, example_four_values_in_db) -> None:
        response = client.post(path=values_url, data={'title': 'The fifth value'})
        response_content = response.json()
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_content == {'message': 'You cant create more than 4 values'}


class TestPrinciplesAPI:
    def test_zero_principles_in_db_should_return_empty_list(self, client):
        response = client.get(principles_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_retrieve_one_principle_should_succeed(self, client, example_single_principle_in_db):
        response = client.get(principles_url)
        response_content = response.json()[0]
        assert response.status_code == status.HTTP_200_OK
        assert response_content['description'] == example_single_principle_in_db.description

    def test_modify_an_existing_value_in_db_should_succeed(self, client, example_single_principle_in_db):
        response = client.put(
            path=principles_url+str(example_single_principle_in_db.id)+'/',
            data={'description': 'New principle'},
            content_type='application/json'
        )
        response_content = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert response_content.get('description') == 'New principle'
        example_single_principle_in_db.refresh_from_db()
        assert example_single_principle_in_db.description == 'New principle'

    def test_delete_principle_in_db_should_succeed(self, client, example_twelve_principles_in_db):
        response = client.get(principles_url)
        assert response.status_code == status.HTTP_200_OK
        assert AgilePrinciples.objects.all().count() == 12
        response = client.delete(path=principles_url + '3/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_create_a_thirteenth_principles_should_fail(self, client, example_twelve_principles_in_db):
        response = client.post(path=principles_url, data={'description': 'another principle should fail'})
        response_content = response.json()
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response_content == {'message': 'You cant create more than 12 principles'}
