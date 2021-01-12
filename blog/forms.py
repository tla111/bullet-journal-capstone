from django import forms
<<<<<<< HEAD

class BlogPostAddForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput)
    post = forms.CharField(widget=forms.Textarea)

=======
>>>>>>> b3b5721825e083bab371a6dd837a749110a6ca31
from .models import BlogModel, CommentModel


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'tags']

<<<<<<< HEAD
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields =['title', 'body', 'tags']
=======
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of Your Achievement', 'id': "paperInputs2"}),
            'body': forms.Textarea(attrs={'placeholder': 'Enter a description of your achievement here'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Keywords of excitement', 'id': "paperInputs2"}),
        }


class CommentForm (forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['context']
>>>>>>> b3b5721825e083bab371a6dd837a749110a6ca31
