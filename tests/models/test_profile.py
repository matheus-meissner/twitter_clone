import pytest

from twitter_app.factories import ProfileFactory

@pytest.fixture
def profile_created():
    return ProfileFactory(bio='testing!')

@pytest.mark.django_db
def test_create_profile(profile_created):
    assert profile_created.bio == 'testing!'
