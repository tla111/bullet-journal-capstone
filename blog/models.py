from django.db import models
from django.utils import timezone
from django.conf import settings


class BlogModel(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=380)
    tags = models.CharField(max_length=100)
    list_date = models.DateTimeField(default=timezone.now)
