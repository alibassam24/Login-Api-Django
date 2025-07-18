from django.db import models
from django.contrib.auth.models import User
#abstractUser vs abstractBaseUser

# Create your models here.

class user(models.Model):
    username=models.CharField()
    password=models.CharField()


    def __str__(self):
        return (f"{self.username}")