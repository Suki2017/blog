from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email',)






