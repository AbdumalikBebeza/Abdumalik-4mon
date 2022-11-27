from django.urls import path
from .views import *
urlpatterns = [
    path('posts/', posts_view),
    path('hashtags/', hashtags_view),
    path('posts/<int:id>/', detail_view),
    path('posts/create/', posts_create_view),
    # path('hastag/create/', hashtags_create_view)
]