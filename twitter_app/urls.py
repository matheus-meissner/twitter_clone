from django.urls import path
from twitter_app import views

urlpatterns = [
    path('tweets/', views.TweetView.as_view(), name='tweets'),
    path('users/', views.ProfileView.as_view(), name='users'),
    path('followers/', views.RelationshipView.as_view(), name='followers'),
]