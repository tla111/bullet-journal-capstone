from django import forms
from .models import BlogModel, CommentModel


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'tags', 'blog_image']
        TAG_STATUS_CHOICES = (
        ('School', 'School'),
        ('Work','Work'),
        ('Lifestyle', 'Lifestyle'),
        ('Organization', 'Organization'),
        ('Time Management', 'Time Management'), 
        )
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Your Blog Title', 'id': "paperInputs2"}),
            'body': forms.Textarea(attrs={'placeholder': 'Write a brief description on how you manage your tasks. What helps you stay organize?'}),
            # 'tags': forms.TextInput(attrs={'placeholder': 'Keywords', 'id': "paperInputs2"}),
        }
        tags = forms.ChoiceField(choices=TAG_STATUS_CHOICES)

class CommentForm (forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['context']
