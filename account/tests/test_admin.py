import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.mark.django_db
def test_users_list(api_client, admin_user):
    api_client.force_login(admin_user)
    user = get_user_model().objects.create_user(
        email='user@example.com',
        password='testpass123',
    )
    url = reverse('admin:account_user_changelist')
    response = api_client.get(url)
    assert user.email
    assert response.status_code == 200



