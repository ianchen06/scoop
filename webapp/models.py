from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class ConnectionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class Connection(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ConnectionType, on_delete=models.CASCADE)
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    authorized_users = models.ManyToManyField(User)
    
    def get_absolute_url(self):
        return reverse('connection-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
