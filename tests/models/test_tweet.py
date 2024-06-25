import pytest

from twitter_app.factories import TweetFactory, CommentFactory
@pytest.fixture
def tweet_posted():
    return TweetFactory(content='testing!')

@pytest.mark.django_db
def test_create_tweet(tweet_posted):
    assert tweet_posted.content == 'testing!'

@pytest.fixture
def comment_posted():
    return CommentFactory(content='Works!!!!')

@pytest.mark.django_db
def test_create_comment(comment_posted):
    assert comment_posted.content == 'Works!!!!'