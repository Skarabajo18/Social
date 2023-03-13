from .models import (
    UserAccount,
    UserProfile,
    UserRelationship,
    USER_TYPE
)

from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm

import datetime


###################################################################
#   Formulario de registro de usuario                             #
###################################################################
class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(
        label = 'Nombres',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'id' : 'input-first-name',
                'placeholder' : 'Ingresa tus nombres'
            }
        )
    )

    last_name = forms.CharField(
        label = 'Apellidos',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'id' : 'input-last-name',
                'placeholder' : 'Ingresa tus apellidos'
            }
        )
    )

    email = forms.EmailField(
        label = 'E-mail',
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'id' : 'input-email',
                'placeholder' : 'Ingresa tu e-mail'
            }
        )
    )

    username = forms.CharField(
        label = 'Nombre de Usuario',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'id' : 'input-username',
                'placeholder' : 'Ingresa el nombre de usuario de la cuenta a crear'
            }
        )
    )


    password1 = forms.CharField(
        label = 'Contraseña',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'id' : 'input-password1',
                'placeholder' : 'Ingresa la contraseña de la cuenta a crear'
            }
        )
    )


    password2 = forms.CharField(
        label = 'Confirma la contraseña',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'id' : 'inp 2',
                'placeholder' : 'Confirma la contraseña'
            }
        )
    )




    class Meta:

        model = UserAccount
        fields = UserCreationForm.Meta.fields + (
            'email', 'username', 'password1', 'password2',
            'first_name', 'last_name',
        )
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
    
    def clean_first_name(self):
        return self.cleaned_data['first_name'].upper()
    
    def clean_last_name(self):
        return self.cleaned_data['last_name'].upper()


