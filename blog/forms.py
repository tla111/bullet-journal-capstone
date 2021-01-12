from django import forms
from .models import BlogModel, CommentModel


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of Your Achievement', 'id': "paperInputs2"}),
            'body': forms.Textarea(attrs={'placeholder': 'Enter a description of your achievement here'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Keywords of excitement', 'id': "paperInputs2"}),
        }


class CommentForm (forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['context']
