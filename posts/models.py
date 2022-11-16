from django.db import models


# Create your models here.
class Post(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField()
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=80)
    posts = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return self.title
