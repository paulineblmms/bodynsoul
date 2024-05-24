from django.forms import ModelForm
from django import forms
from main.models import Report, Data

class ProblemReport(ModelForm):
    class Meta:
        model = Report
        fields = ["username", "description"]

class CalorieTrackingForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Data.objects.all(), empty_label=None)

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['category', 'description', 'kilocalories', 'protein', 'fat', 'carbohydrate']

class StatsForm(forms.Form):
    weight = forms.FloatField()
    height = forms.FloatField()
    age = forms.IntegerField()
    fields = ['weight', 'height', 'age']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)