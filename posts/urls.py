from django.urls import path
from .views import *
urlpatterns = [
    path('posts/', PostsVIew.as_view()),
    path('hashtags/', HashtagView.as_view()),
    path('posts/<int:id>/', DetailPostView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
]