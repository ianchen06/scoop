from django import forms

from .models import Connection

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        optional_fields = kwargs.pop("optional_fields", [])
        super(ConnectionForm, self).__init__(*args, **kwargs)
        for f in optional_fields:
            self.fields[f].required = False
