from django import forms
from .models import Comment,Post
from django_ckeditor_5.fields import CKEditor5Field

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Enter your comment here...', 'style': 'color: white;'})
        }
        labels = {
            'text': 'Comment'
        }


class PostForm(forms.ModelForm):
    content = CKEditor5Field(config_name='extends')
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title of your post'}),
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 50, 'placeholder': 'Write your post content here...'}),
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image'
        }
