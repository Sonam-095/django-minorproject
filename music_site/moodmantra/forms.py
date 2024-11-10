from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import signup

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email',
        'id':'email',
        'autocomplete': 'email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password',
        'id':'password',
        'autocomplete': 'current-password'
    }))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Check if user exists in the database
        try:
            user = signup.objects.get(Email=email)
            if user.Password != password:
                raise ValidationError('Invalid email or password.')
        except signup.DoesNotExist:
            raise ValidationError('Invalid email or password.')

        return cleaned_data


class SignupForm(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['Name', 'Email', 'Password']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
