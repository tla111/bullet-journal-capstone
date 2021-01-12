from django.db import models


from django.contrib.auth.models import timezone
from journaluser.models import BulletJournalUser
# Create your models here.

from django.utils import timezone
from django.conf import settings


class BlogModel(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=380)
    tags = models.CharField(max_length=100)
    list_date = models.DateTimeField(default=timezone.now)
<<<<<<< HEAD
    like_dislike_choices = (('Like', 'Like'), ('Dislike', 'Dislike'))
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    like_dislike_post = models.BooleanField(choices=like_dislike_choices)

class CommentModel(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=250)
    list_date = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=100)

=======

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    post = models.ForeignKey(
        BlogModel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    context = models.TextField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)
>>>>>>> b3b5721825e083bab371a6dd837a749110a6ca31
