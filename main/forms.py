from django.forms import ModelForm
from django import forms
from main.models import Report, Data, Mood

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
    activity_level = forms.ChoiceField(choices=[
        ('sedentary', 'Sedentary'),
        ('lightly_active', 'Lightly Active'),
        ('moderately_active', 'Moderately Active'),
        ('very_active', 'Very Active'),
        ('extra_active', 'Extra Active'),
    ])
    fields = ['weight', 'height', 'age', 'activity_level']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
