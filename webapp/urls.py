from django.urls import path

import webapp.views as v

urlpatterns = [
    path('connections/', v.ConnectionList.as_view(), name='connection-list'),
    path('connections/create/', v.ConnectionCreate.as_view(), name='connection-create'),
    path('connections/<int:pk>/', v.ConnectionDetailView.as_view(), name='connection-detail'),
    path('connections/<int:pk>/update/', v.ConnectionUpdate.as_view(), name='connection-update'),
    path('connections/<int:pk>/delete/', v.ConnectionDelete.as_view(), name='connection-delete'),
]
