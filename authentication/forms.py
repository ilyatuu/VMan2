from django import forms
from .models import *
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
                  'first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2'
                  ]
        exclude = ['username']

class ProfileForm(forms.ModelForm):
    mobile_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget(
        initial='TZ',
        attrs={'placeholder': 'Mobile number'}
        )
    )

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user_token', 'user', 'created_at', 'updated_at']
