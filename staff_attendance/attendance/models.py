from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ユーザID")
    email = models.EmailField(verbose_name="メールアドレス")
