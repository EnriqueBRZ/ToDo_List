from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django. contrib.auth.models import User

class FormHomework(forms.Form):

    title = forms.CharField(
        label="Título",
        max_length=25,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Título'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñíóáúé ]*$', 'El título no debe contener caracteres especiales','invalid_title'),
        ]
    )
    
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(150, 'Te has pasado, solo puedes ingresar 150 caracteres')
        ]
    )

    content.widget.attrs.update({
        'placeholder': 'Descripción'
    })

    status_options = [
        (1, 'Completado'),
        (0, 'Pendiente')
    ]

    status = forms.TypedChoiceField(
        label="Estatus",
        choices = status_options,
    )


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']