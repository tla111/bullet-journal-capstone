from django.db import models
from django.contrib.auth.models import timezone
from journaluser.models import BulletJournalUser
# Create your models here.

class BlogPosts(models.Model):
    title = models.CharField(max_length=250)
    post = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    journal_user = models.ForeignKey(BulletJournalUser, on_delete=models.CASCADE)




