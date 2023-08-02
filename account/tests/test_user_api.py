import pytest
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

URL = reverse('user:register')
TOKEN_URL = reverse('user:token')
USER_DETAIL_URL = reverse('user:user-detail')


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
    assert res.status_code == status.HTTP_201_CREATED
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
    assert response.status_code == status.HTTP_400_BAD_REQUEST


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
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert not user


@pytest.mark.django_db
def test_create_token_for_user(api_client):
    user_details = {
        'email': 'test@example.com',
        'password': 'testpass123',
        'full_name': 'Test Name'
    }
    create_user(**user_details)
    payload = {'email': user_details['email'],
               'password': user_details['password']}
    response = api_client.post(TOKEN_URL, payload)
    assert 'token' in response.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_token_with_bad_credentials(api_client):
    """ Test creating a user with blank password"""

    user_details = {
        'email': 'test@example.com',
        'password': 'goodpassword',
        'full_name': 'Test Name'
    }
    payload = {
        'email': user_details['email'],
        'password': 'badpassword'
    }
    create_user(**user_details)
    response = api_client.post(TOKEN_URL, payload)
    assert 'token' not in response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_create_token_blank_password(api_client):
    """ Test creating a user with blank password"""

    payload = {
        'email': 'test@example.com',
        'password': ''
    }
    response = api_client.post(TOKEN_URL, payload)
    assert 'token' not in response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_retrieve_user_unauthorized(api_client):
    response = api_client.get(USER_DETAIL_URL)
    assert response.status_code == status.HTTP_403_FORBIDDEN


