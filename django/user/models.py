from django.db import models
from django.contrib.auth.models import User

class RegisterToken(models.Model):
    token = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
