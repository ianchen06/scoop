from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from dal import autocomplete

from .models import Connection, Destination
from .forms import ConnectionForm
from .tables import ConnectionTable
from .filters import ConnectionFilter

# Create your views here.
class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return User.objects.none()
        qs = User.objects.all()
        if self.q:
            qs = qs.filter(username__icontains=self.q)
        return qs

class DestinationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Destination.objects.none()
        qs = Destination.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

class ConnectionList(ListView):
    model = Connection

class FilteredConnectionListView(SingleTableMixin, FilterView):
    table_class = ConnectionTable
    model = Connection
    template_name = 'webapp/connection_list.html'
    filterset_class = ConnectionFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Connection.objects.all().select_related('type')
        else:
            return Connection.objects.filter(authorized_users=self.request.user).select_related('type')

class ConnectionDetailView(DetailView):
    model = Connection

class ConnectionCreate(CreateView):
    model = Connection
    form_class = ConnectionForm
    success_url = reverse_lazy('connection-list')

class ConnectionUpdate(UpdateView):
    model = Connection
    form_class = ConnectionForm
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        data = form.save(commit=False)
        obj = self.model.objects.get(id=form.instance.id)
        if not data.password:
            data.password = obj.password
        self.object = data.save()
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'optional_fields': ['authorized_users'],
            'current_user': self.request.user
            })
        return kwargs

class ConnectionDelete(DeleteView):
    model = Connection
    success_url = reverse_lazy('connection-list')
