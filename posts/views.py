from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Hashtag, Comment
from posts.forms import PostCreateForm, CommentCreateForm, HashtagCraeteForm


# Create your views here.
def posts_view(request):
    if request.method == 'GET':
        hashtag_id = request.GET.get('hashtag_id')
        if hashtag_id:
            posts = Post.objects.filter(hashtag=Hashtag.objects.get(id=hashtag_id))
        else:
            posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=context)


def hashtags_view(request, **kwargs):
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
            'comments': Comment.objects.filter(id=kwargs['id']),
            'form': CommentCreateForm
        }
        return render(request, 'posts/detail.html', context=data)

    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                author_id=1,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            post = Post.objects.get(id=kwargs['id'])
            data = {
                'post': post,
                'comments': Comment.objects.filter(post_id=kwargs['id']),
                'form': CommentCreateForm
            }
            return render(request, 'posts/detail.html', context=data)

        else:
            post = Post.objects.get(id=kwargs['id'])
            comment = Comment.objects.filter(post_id=post)
            data = {
                'post': post,
                'comments': comment,
                'form': CommentCreateForm
            }
            return render(request, 'posts/detail.html', context=data)


def posts_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create_post.html', context=data)
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                # photo=form.cleaned_data.get('photo'),
                likes=form.cleaned_data.get('likes'),
                hashtag=form.cleaned_data.get('hashtag')
            )
            return redirect('/posts')
        else:
            data = {
                'form': form
            }
            return render(request, 'posts/create_post.html', context=data)


def hashtags_create_view(request):
    if request.method == 'GET':
        data = {
            'form': HashtagCraeteForm
        }
        return render(request, 'posts/create_hashtag.html', context=data)
    elif request.method == 'POST':
        form = HashtagCraeteForm(data=request.POST)
        if form.is_valid():
            Hashtag.objects.create(
                title=form.cleaned_data.get('title')
            )
            return redirect('/hashtags/')
        else:
            data = {
                'form': form
            }
            return render(request, 'posts/create_hashtag.html', context=data)
