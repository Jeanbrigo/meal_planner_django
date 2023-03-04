from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.TextField()
    dayToEat=models.CharField(max_length=100)
    ingredients=models.CharField(max_length=100)
    