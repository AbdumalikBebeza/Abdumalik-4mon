from django.shortcuts import render, HttpResponse
from .models import Post, Hashtag, Comment


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


def detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        print(post.title)
        data = {
            'post': post,
            'comments': Comment.objects.filter(post_id=kwargs['id'])
        }
        return render(request, 'posts/detail.html', context=data)