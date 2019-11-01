from django.contrib.auth.forms import AuthenticationForm

from .models import Scientist


class ScientistLoginForm(AuthenticationForm):
    class Meta:
        model = Scientist
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ScientistLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


"""class ScientistRegistrationForm(UserCreationForm):
    class Meta:
        model = Scientist
        fields = ('first_name', 'last_name', 'position', 'username', 'password')

    def __init__(self, *args, **kwargs):
        super(ScientistRegistrationForm, self).__init__ (*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'"""
