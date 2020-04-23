from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .models import Connection
from .forms import ConnectionForm
from .tables import ConnectionTable
from .filters import ConnectionFilter

# Create your views here.
class ConnectionList(ListView):
    model = Connection

class FilteredConnectionListView(SingleTableMixin, FilterView):
    table_class = ConnectionTable
    model = Connection
    template_name = 'webapp/connection_list.html'
    filterset_class = ConnectionFilter

class ConnectionDetailView(DetailView):
    model = Connection

class ConnectionCreate(CreateView):
    model = Connection
    form_class = ConnectionForm
    success_url = reverse_lazy('connection-list')

class ConnectionUpdate(UpdateView):
    model = Connection
    form_class = ConnectionForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'optional_fields': ['authorized_users'],
            'current_user': self.request.user
            })
        return kwargs

class ConnectionDelete(DeleteView):
    model = Connection
    success_url = reverse_lazy('connection-list')
