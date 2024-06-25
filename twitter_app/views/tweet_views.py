from django.http import HttpResponse
from django.views import generic
from twitter_app.models.tweet import Tweet
from twitter_app.models.profile import Profile, Relationship


class TweetView(generic.View):
    def get(self, request, *args, **kwargs):
        t = Tweet.objects.filter()

        return HttpResponse(t)

class ProfileView(generic.View):
    def get(self, request, *args, **kwargs):
        p = Profile.objects.filter()
        return HttpResponse(p)
    
class RelationshipView(generic.View):
    def get(self, request, *args, **kwargs):
        r = Relationship.objects.filter()
        return HttpResponse(r)