from django import forms

class BlogPostAddForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    post = forms.CharField(widget=forms.Textarea)

from .models import BlogModel, CommentModel


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields =['title', 'body', 'tags']