from django import forms
from django.core.validators import RegexValidator

from dal import autocomplete

from .models import Connection

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = '__all__'
        widgets = {
                'authorized_users': autocomplete.ModelSelect2Multiple(url='user-autocomplete',attrs={'data-container-css-class': ''}),
                'authorized_destinations': autocomplete.ModelSelect2Multiple(url='destination-autocomplete',attrs={'data-container-css-class': ''}),
                'password': forms.PasswordInput()
                }
    def __init__(self, *args, **kwargs):
        # Modify the form fields here to preseve automitically set attributes
        optional_fields = kwargs.pop("optional_fields", [])
        current_user = kwargs.pop("current_user", None)
        super(ConnectionForm, self).__init__(*args, **kwargs)
        self.fields['name'].validators = [RegexValidator('^[a-zA-Z0-9_]+$')]
        for f in optional_fields:
            self.fields[f].required = False
        if current_user:
            if not current_user.is_superuser:
                self.fields['authorized_users'].disabled = True
                self.fields['authorized_destinations'].disabled = True
            else:
                self.fields['password'].required = False


