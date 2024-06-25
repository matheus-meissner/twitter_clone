import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_tweet_view(client):
    url = reverse('tweets')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_users_view(client):
    url = reverse('users')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_relationship_view(client):
    url = reverse('followers')
    response = client.get(url)
    assert response.status_code == 200