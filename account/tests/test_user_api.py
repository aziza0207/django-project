import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

URL = reverse('user:register')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


@pytest.mark.django_db
def test_create_user_success(api_client):
    payload = {
        'email': 'test@example.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123',
        'full_name': 'Test Name'
    }
    res = api_client.post(URL, payload)
    user = get_user_model().objects.get(email=payload['email'])
    assert res.status_code == 201
    assert user.check_password(payload['password'])


@pytest.mark.django_db
def test_user_with_email_exists_error(api_client):
    payload = {
        'email': 'test@example.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123',
        'full_name': 'Test Name'
    }
    payload1 = {
        'email': 'test@example.com',
        'password': 'testpass123',
        'full_name': 'Test Name'
    }
    create_user(**payload1)
    response = api_client.post(URL, payload)
    assert response.status_code == 400


@pytest.mark.django_db
def test_password_too_short_error(api_client):
    payload = {
        'email': 'test@example.com',
        'password': 'pw',
        'confirm_password': 'pw',
        'full_name': 'Test Name'
    }
    response = api_client.post(URL, payload)
    user = get_user_model().objects.filter(email=payload['email']).exists()
    assert response.status_code == 400
    assert not user
