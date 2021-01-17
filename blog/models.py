from django.db import models
from django.utils import timezone
from django.conf import settings


class BlogModel(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_image = models.ImageField(null=True, blank=True, upload_to="blogimages/" )
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=380)
    list_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    TAG_STATUS_CHOICES = (
        ('School', 'School'),
        ('Work','Work'),
        ('Lifestyle', 'Lifestyle'),
        ('Organization', 'Organization'),
        ('Time Management', 'Time Management'), 
    )
    tags = models.CharField(
        max_length=100,
        choices=TAG_STATUS_CHOICES,
        blank=True,
        null=True,
        default=None,
        )
    

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    post = models.ForeignKey(
        BlogModel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    context = models.TextField(max_length=280)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)