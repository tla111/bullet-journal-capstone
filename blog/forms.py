from django import forms


from .models import BlogModel, CommentModel


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'tags']


class CommentForm (forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['context']

