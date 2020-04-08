from django.urls import path

from . import views

urlpatterns = [
    path('connection/', views.connection_list, name='connection_list'),
    path('connection/<int:pk>/edit/', views.connection_edit, name='connection_edit'),
    path('connection/<int:pk>/', views.connection_detail, name='connection_detail'),
    path('connection/new/', views.connection_new, name='connection_new'),
]

