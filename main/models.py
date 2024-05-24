from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    kilocalories = models.IntegerField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()

    def __str__(self):
        return self.description

class Report(models.Model):
    username = models.CharField(max_length=255)
    date_time = models.DateField(auto_now_add=True)
    description = models.TextField()

class CalorieTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Data, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s tracking - {self.item.description}"
    
class Stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    age = models.IntegerField()
    activity_level = models.CharField(max_length=100, default='moderately_active')