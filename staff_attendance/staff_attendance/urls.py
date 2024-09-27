from django.contrib import admin
from django.urls import path
from .views import FrontPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", FrontPage.as_view())
]
