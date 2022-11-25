from django import forms
from posts.models import Hashtag, Post

CATEGORY_CHOISES = (
    (hashtag.id, hashtag.title,) for hashtag in Hashtag.objects.all()
)
POST_CHOISES = (
    (post.id, post.title) for post in Post.objects.all()
)


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=3)
    # photo = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea, min_length=3)
    likes = forms.IntegerField()
    hashtag = forms.ChoiceField(choices=CATEGORY_CHOISES)


class CommentCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Добавьте Комментарий")


class HashtagCraeteForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea, max_length=150, min_length=2, label="Добавте Хэштэг")
