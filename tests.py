import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("Ivan", "ivan@deer.com", "passwirdio")
    assert User.objects.count() == 1
