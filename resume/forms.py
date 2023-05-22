from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        'placeholder': 'First Name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        'placeholder': 'Last Name',
    }))

    career_interest = forms.CharField(widget=forms.TextInput(attrs={  # new field
        'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        'placeholder': 'Career Interest',
    }), required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'career_interest']
