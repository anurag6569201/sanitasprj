from django import forms
from django.forms.widgets import ClearableFileInput
from .models import UserProfile,Sanitizer
from .models import TrendingData

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = 'name','surname','mobile_number','address','postcode','area','email','education','country','state_region','profile_image'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'state_region': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'}),
        }

class SanitizerForm(forms.ModelForm):
    class Meta:
        model = Sanitizer
        fields ='name','street','city','state','zip','contactperson','phone','email','certificate','isChecked','profile_image','CPphone','CPemail','longitude','latitude'

from .models import Disease

from django.forms import formset_factory
from .models import Disease

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['name', 'cases']

DiseaseFormSet = formset_factory(DiseaseForm, extra=10)

class TrendingDataForm(forms.ModelForm):
    class Meta:
        model=TrendingData
        fields=['city','state']
