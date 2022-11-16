from django.shortcuts import render
from .models import Post, Hashtag


# Create your views here.
def posts_view(request):
    if request.method == 'GET':
        context = {
            'posts': Post.objects.all()
        }
        return render(request, 'posts/posts.html', context=context)


def hashtags_view(request):
    if request.method == 'GET':
        context = {
            'hashtags': Hashtag.objects.all()
        }
        return render(request, 'posts/hashtags.html', context=context)