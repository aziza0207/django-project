import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_user_with_email():
    email = 'test@example.com'
    password = 'testpass123'
    user = get_user_model().objects.create_user(email=email, password=password)
    assert user.email == email
    assert user.check_password(password)


@pytest.mark.django_db
def test_user_email_normalized():
    sample_emails = [
        ['test1@EXAMPLE.com', 'test1@example.com'],
        ['Test2@Example.com', 'Test2@example.com'],
        ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
        ['test4@example.COM', 'test4@example.com'],
    ]
    for email, expected in sample_emails:
        user = get_user_model().objects.create_user(email=email,
                                                    password='sample123')
        assert user.email == expected


@pytest.mark.django_db
def test_create_superuser():
    user = get_user_model().objects.create_superuser(
        'test@example.com',
        'test123'
    )
    assert user.is_superuser
    assert user.is_staff
