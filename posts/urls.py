from django.urls import path
from .views import *
urlpatterns = [
    path('posts/', posts_view),
    path('hashtags/', hashtags_view)
]