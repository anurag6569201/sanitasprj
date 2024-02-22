from django import forms
from .models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Enter your comment here...'})
        }
        labels = {
            'text': 'Comment'
        }


class PostForm(forms.ModelForm):
    class Meta:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["text"].required = False
            
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
