from django.db import models

class RegisterToken(models.Model):
    token = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
