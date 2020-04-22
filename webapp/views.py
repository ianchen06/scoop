from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Connection
from .forms import ConnectionForm

# Create your views here.
def connection_list(request):
    connections = Connection.objects.all().order_by('id')
    paginator = Paginator(connections, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'connection_list.html', {'page_obj': page_obj})

def connection_detail(request, pk):
    connection = get_object_or_404(Connection, pk=pk)
    return render(request, 'connection_detail.html', {'connection': connection})

def connection_new(request):
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            connection = form.save(commit=False)
            connection.save()
            return redirect('connection_detail', pk=connection.pk)
    else:
        form = ConnectionForm()
    return render(request, 'connection_new.html', {'form': form})

def connection_edit(request, pk):
    connection = get_object_or_404(Connection, pk=pk)
    if request.method == "POST":
        form = ConnectionForm(request.POST, instance=connection)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('connection_detail', pk=connection.pk)
    else:
        form = ConnectionForm(instance=connection)
    return render(request, 'connection_new.html', {'form': form})
