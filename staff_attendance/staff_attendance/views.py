from django.shortcuts import render, redirect
from django.views import View

class LogIn(View):
    def get(self, request):
        return render(request, "staff_attendance/login.html")
