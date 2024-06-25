import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from twitter_app.models import Tweet,Profile

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())


    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
            return user
        
class TweetFactory(factory.django.DjangoModelFactory):
    content = factory.LazyAttribute(lambda x: faker.sentence())
    user = factory.SubFactory(UserFactory)
    created_at = factory.LazyAttribute(lambda x: now())

    class Meta:
        model = Tweet

class ProfileFactory(factory.django.DjangoModelFactory):
    bio = factory.LazyAttribute(lambda x: faker.sentence())
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Profile
