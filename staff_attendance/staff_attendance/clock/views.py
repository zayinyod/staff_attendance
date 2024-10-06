from django.shortcuts import render, redirect
from django.views import View

class Clock(View):
    def get(self, request):
        return render(request, "staff_attendance/clock.html")
