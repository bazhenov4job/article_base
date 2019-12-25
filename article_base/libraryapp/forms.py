from django import forms
from .models import Article, Authors, Themes, Sources, References


class AuthorCreationForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AuthorCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ThemeCreationForm(forms.ModelForm):
    class Meta:
        model = Themes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ThemeCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class SourceCreationForm(forms.ModelForm):
    class Meta:
        model = Sources
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SourceCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ReferenceCreationForm(forms.ModelForm):
    class Meta:
        model = References
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReferenceCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArticleCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
