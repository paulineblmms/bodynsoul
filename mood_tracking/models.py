from django.db import models

# Create your models here.

class Mood(models.Model):
    mood = models.CharField(max_length=100)
    food_intake = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.date}: {self.mood}"
