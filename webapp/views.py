from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Connection
from .forms import ConnectionForm

# Create your views here.
class ConnectionList(ListView):
    model = Connection

class ConnectionDetailView(DetailView):
    model = Connection

class ConnectionCreate(CreateView):
    model = Connection
    form_class = ConnectionForm
    success_url = reverse_lazy('connection-list')

class ConnectionUpdate(UpdateView):
    model = Connection
    fields = ['name', 'host', 'port', 'username', 'password']

class ConnectionDelete(DeleteView):
    model = Connection
    success_url = reverse_lazy('connection-list')
