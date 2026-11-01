from django.db import models

class User(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200,unique=True)
    superuser = models.BooleanField(default=False)    
    active = models.BooleanField(default=True)

