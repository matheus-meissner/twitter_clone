from django.views import generic
from twitter_app.models.tweet import Tweet

class TweetView(generic.ListView):
        queryset = Tweet.objects.filter().order_by('-created_at')
        template_name = 'index.html'
 