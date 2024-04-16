from django import forms
from home.models import spherepost

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
