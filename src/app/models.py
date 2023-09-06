from django.db import models
from django_cryptography.fields import encrypt

# Create your models here.
class UserAccount(models.Model):
    name = models.CharField("帳號", max_length=36)
    password = encrypt(models.CharField("密碼", max_length=48, blank=True, null=True))