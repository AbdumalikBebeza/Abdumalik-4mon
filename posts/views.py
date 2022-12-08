from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Hashtag, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from users.utils import get_user_from_request
from django.views.generic import ListView, CreateView, DetailView
PAGINATION_LIMIT = 4


class HashtagView(ListView):
    model = Hashtag
    template_name = 'posts/hashtags.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'object_list': self.get_queryset(),
            'user': get_user_from_request(self.request)
        }
        return context


class DetailPostView(DetailView, CreateView):
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    form_class = CommentCreateForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        return {
            'post': self.get_object(),
            'comments': Comment.objects.filter(post=self.get_object()),
            'form': kwargs.get('form', self.form_class),
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author=request.user,
                text=form.cleaned_data.get('text'),
                post_id=self.get_object().id
            )
            return redirect(f'/posts/{self.get_object().id}/')
        return render(request, self.template_name, context=self.get_context_data(form=form))


class PostsVIew(ListView):
    template_name = 'posts/posts.html'
    queryset = Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        hashtag_id = self.request.GET.get('hashtag_id')
        search_text = self.request.GET.get('search')
        page = int(self.request.GET.get('page', 1))
        if hashtag_id:
            posts = Post.objects.filter(hashtag=Hashtag.objects.get(id=hashtag_id))
        else:
            posts = Post.objects.all()
        if search_text:
            posts = posts.filter(title__icontains=search_text)

        max_page = round(posts.__len__() / PAGINATION_LIMIT)
        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]
        return {
            'posts': posts,
            'user': get_user_from_request(self.request),
            'current_page': page,
            'max_page': list(range(1, max_page + 1)),
            'hashtag_id': hashtag_id,
            'search_text': search_text
        }


class PostCreateView(ListView, CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
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
            return render(request, self.template_name, context=self.get_context_data(form=form))
