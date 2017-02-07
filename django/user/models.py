from django.db import models

from gomoku.settings import TOKEN_LEN

class RegisterToken(models.Model):
    token = models.CharField(max_length=TOKEN_LEN)
    email = models.EmailField()
    password = models.CharField(max_length=TOKEN_LEN)
