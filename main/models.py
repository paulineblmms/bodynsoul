from django.db import models

class Data(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    kilocalories = models.IntegerField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()

    def __str__(self):
        return self.description
    
    from django.db import models

class Report(models.Model):
    username = models.CharField(max_length=255)
    date_time = models.DateField(auto_now_add=True)
    description = models.TextField()