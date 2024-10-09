from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from datetime import datetime
from zoneinfo import ZoneInfo

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="部署名")

    def __str__(self):
        return self.name

def create_id():
    return get_random_string(6)

class User(AbstractUser):
    user_id = models.CharField(
        primary_key=True, default=create_id, max_length=6, editable=False, verbose_name="ユーザID")
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, verbose_name="部署名")
    # アイコン, 有給, 二要素認証

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.email}, {self.department}"

class Clock(models.Model):
    datetime_now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y.%m.%d %H:%M:%S")

    clock_status = [
        ("clock_in", "出勤"),
        ("clock_out", "退勤"),
    ]

    location_status = [
        ("office", "オフィス"),
        ("telework", "在宅"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="ユーザ名")
    time_stamp = models.DateTimeField(default=datetime_now, verbose_name="日時")
    clock = models.CharField(max_length=20, choices=clock_status, verbose_name="in/out")
    break_time = models.IntegerField(default=1, verbose_name="休憩時間")
    location = models.CharField(max_length=20, default="office", choices=location_status, verbose_name="勤務場所")
    # 丸め計算, 深夜時間, 残業時間, 合計勤務時間, 給与, 有給, 交通費

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "time_stamp", "clock"],
                name="clock_unique",
            )
        ]

    def __str__(self):
        return f"{self.user.user_id}, {self.user.username}, {self.time_stamp}"

# class workflow:
# ユーザ作成/削除
# 承認ルート作成/削除
# 申請/承認（有給申請, 打刻修正, 勤怠締め）
