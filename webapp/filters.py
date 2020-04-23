import django_filters

from .models import Connection

class ConnectionFilter(django_filters.FilterSet):
    class Meta:
        model = Connection
        fields = ['name', 'host']
