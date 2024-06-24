from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Tweet by {self.user.username}: {self.content[:20]}...'

    class Meta:
        ordering = ['-created_at']

class Comments(models.Model):
    tweetTarget = models.ForeignKey(Tweet, related_name='Comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username}: {self.content[:20]}...'

    class Meta:
        ordering = ['-created_at']