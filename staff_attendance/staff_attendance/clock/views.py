from django.shortcuts import render, redirect
from django.views import View
from .forms import ClockForm

class Clock(View):
    def get(self, request):
        form = ClockForm()
        return render(request, "staff_attendance/clock.html", {"form": form})

    def post(self, request):
        form = ClockForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("staff_attendance:clock")
        return render(request, "staff_attendance/clock.html", {"form": form})
