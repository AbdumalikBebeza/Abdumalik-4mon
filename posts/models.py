from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(choices=((i, "*" * i) for i in range(1, 6)), null=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=80)
    posts = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}, {self.text}'
