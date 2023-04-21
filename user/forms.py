from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
        ]

class GroupForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })