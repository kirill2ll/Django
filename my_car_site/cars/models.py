from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.year}"

class Review(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    stars = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.stars}"