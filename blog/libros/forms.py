from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
