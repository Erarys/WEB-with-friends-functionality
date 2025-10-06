from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class EmailUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email']
        field_classes = {'email': forms.EmailField}


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
