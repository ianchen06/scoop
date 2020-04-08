from django import forms

from .models import Connection

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ('name', 'host', 'port', 'username', 'password',)
