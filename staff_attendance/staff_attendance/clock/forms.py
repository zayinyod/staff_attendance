from django.forms import ModelForm
from attendance.models import Clock

class ClockForm(ModelForm):
    class Meta:
        model = Clock
        fields = ["time_stamp", "clock", "break_time", "location"]
