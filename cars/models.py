from django.db import models


class Car(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    team = models.CharField(max_length=100)
    car_identification = models.CharField(max_length=7, unique=True)
    car_model = models.CharField(max_length=200)
    cars_per_team = models.IntegerField()

    def __str__(self):
        return self.car_identification
