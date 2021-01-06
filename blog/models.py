from django.db import models
<<<<<<< HEAD
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




=======
# from journaluser.models import BulletJournalUser
# from django.utils import timezone



# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     blog_content = models.TextField()
#     date = models.DateTimeField(default=timezone.now)
#     user = models.ForeignKey(BulletJournalUser, on_delete=models.CASCADE, related_name="blog_user", blank=True, null=True, default=None)

#     def __str__(self):
#         return self.title

# See if Team like or not!
# Did not migrate...
>>>>>>> 80c5cbb4bdbea7a49a5c9e58846f70f2fb80d7fa
