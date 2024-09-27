from django.shortcuts import render
from django.views import View

# def frontpage(request):
#     return render(request, "staff_attendance/frontpage.html")

class FrontPage(View):
    def get(self, request):
        return render(request, "staff_attendance/frontpage.html")
