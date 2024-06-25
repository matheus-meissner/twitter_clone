from django.http import HttpResponse
from django.views import generic
from twitter_app.models.tweet import Tweet, Comments

class TweetView(generic.View):
    def get(self, request, *args, **kwargs):
        t = Tweet.objects.filter()
        return HttpResponse(t)
    
class CommentsView(generic.View):
    def get(self, request, *args, **kwargs):
        c = Comments.objects.filter()
        return HttpResponse(c)
