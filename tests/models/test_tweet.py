import pytest

from twitter_app.factories import TweetFactory

@pytest.fixture
def tweet_posted():
    return TweetFactory(content='testing!')

@pytest.mark.django_db
def test_create_tweet(tweet_posted):
    assert tweet_posted.content == 'testing!'
