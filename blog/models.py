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

