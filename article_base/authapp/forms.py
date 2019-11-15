from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from django import forms
from .models import Scientist


class ScientistLoginForm(AuthenticationForm):
    class Meta:
        model = Scientist
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ScientistLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ScientistRegistrationForm(UserCreationForm):
    class Meta:
        model = Scientist
        fields = ('first_name', 'last_name', 'position', 'username', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super(ScientistRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean(self):
        cleaned_data = super(ScientistEditForm, self).clean()
        if not (cleaned_data['first_name'].istitle()):
            raise ValidationError("Имя должно начинаться с заглавной буквы")
        return cleaned_data


class ScientistEditForm(UserChangeForm):
    class Meta:
        model = Scientist
        fields = ('first_name', 'last_name', 'position', 'username', 'password', 'email')

    def __init__(self, *args, **kwargs):
        super(ScientistEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super(ScientistEditForm, self).clean()
        if not(cleaned_data['first_name'].istitle()):
            raise ValidationError("Имя должно начинаться с заглавной буквы")
        return cleaned_data
