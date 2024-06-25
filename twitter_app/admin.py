from django.contrib import admin
from .models.profile import Profile, Relationship, User
from .models.tweet import Tweet

admin.site.register(Profile)
admin.site.register(Relationship)
admin.site.register(Tweet)
