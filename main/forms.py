from django.forms import ModelForm
from main.models import Report

class ProblemReport(ModelForm):
    class Meta:
        model = Report
        fields = ["username", "description"]