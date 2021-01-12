from django.contrib import admin
from .models import BlogModel, CommentModel

admin.site.register(BlogModel)
admin.site.register(CommentModel)
