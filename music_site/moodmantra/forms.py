from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import signup

class loginform(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['Email', 'Password']

        def clean(self):
            cleaned_data = super().clean()
            email = cleaned_data.get('Email')
            password = cleaned_data.get('Password')

            if email and password:
                # Authenticate the user without checking for duplicates
                user = authenticate(email=email, password=password)
                if user is None:
                    raise forms.ValidationError('Invalid email or password.')

            return cleaned_data
        
class signupform(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['Name', 'Email', 'Password']