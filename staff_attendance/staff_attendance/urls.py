from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import LogIn

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LogIn.as_view(), name="login"),
    path("clock/", include("staff_attendance.clock.urls")),
]
