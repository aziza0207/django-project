import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def admin_user():
    return get_user_model().objects.create_superuser(
        email='admin@example.com',
        password='testpass123',
    )


@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        email='user@example.com',
        password='testpass123',
        full_name='Test Name'
    )
