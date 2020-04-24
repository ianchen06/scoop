import django_tables2 as tables
from django_tables2 import A

from .models import Connection

class ConnectionTable(tables.Table):
    name = tables.Column(linkify=("connection-update", [tables.A("pk")]))
    class Meta:
        model = Connection
        fields = ['type', 'name', 'host', 'port', 'username']
