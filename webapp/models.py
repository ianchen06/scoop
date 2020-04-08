from django.db import models

# Create your models here.
class Connection(models.Model):
    name = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    authorized_users = models.TextField()
