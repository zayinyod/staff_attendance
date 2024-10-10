from django.urls import path
from .views import Clock

urlpatterns = [
    path("", Clock.as_view(), name="clock"),
]
