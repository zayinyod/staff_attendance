from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from datetime import datetime
from zoneinfo import ZoneInfo

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Department")

    def __str__(self):
        return self.name

def create_id():
    return get_random_string(6)

class User(AbstractUser):
    user_id = models.CharField(
        primary_key=True, default=create_id, max_length=6, editable=False, verbose_name="User ID")
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, verbose_name="Department")

    def __str__(self):
        return f"{self.user_id}; {self.username}; {self.email}; {self.department}"

class Clock(models.Model):
    now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")

    clock_status = [
        ("clock_in", "In"),
        ("clock_out", "Out"),
    ]

    location_status = [
        ("office", "Office"),
        ("telework", "Telework"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Username")
    time_stamp = models.DateTimeField(default=now, verbose_name="Datetime")
    clock = models.CharField(max_length=20, default="In", choices=clock_status, verbose_name="In/Out")
    break_time = models.IntegerField(default=1, verbose_name="Break time")
    location = models.CharField(max_length=20, default="Office", choices=location_status, verbose_name="Location")

    class Meta:
        unique_together = ("user", "time_stamp", "clock")

    def __str__(self):
        return f"{self.user.user_id}; {self.user.username}; {self.time_stamp}"

# class workflow:
