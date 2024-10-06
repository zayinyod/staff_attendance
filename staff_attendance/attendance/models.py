from django.db import models
from django.utils.crypto import get_random_string
import uuid

def create_id():
    return get_random_string(6)

class User(models.Model):
    id = models.CharField(
        primary_key=True, default=create_id, max_length=22, editable=False, verbose_name="ユーザID")
    name = models.CharField(max_length=50, verbose_name="ユーザ名")
    email = models.EmailField(verbose_name="メールアドレス")

# class department(models.Model):
# class Clock(models.Model):
