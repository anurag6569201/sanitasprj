from django import forms
from home.models import spherepost,sphereComment

class sphereForm(forms.ModelForm):
    class Meta:
        model = spherepost
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Whats is happening !', 'style': 'resize:none;'}),
        }
        labels = {
            'content': 'content',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = sphereComment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Enter your comment here...', 'style': 'color: white;'})
        }
        labels = {
            'text': 'Comment'
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')