from django.db import models
from django.urls import reverse

# Create your models here.
class Connection(models.Model):
    name = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    authorized_users = models.TextField()
    
    def get_absolute_url(self):
        return reverse('connection-detail', kwargs={'pk': self.pk})

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
