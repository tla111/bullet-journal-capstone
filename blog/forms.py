from django import forms

from blog.models import BlogPosts

class BlogPostAddForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    post = forms.CharField(widget=forms.Textarea)

from .models import BlogModel


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'tags']

