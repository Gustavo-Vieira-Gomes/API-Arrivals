from django.db import models

# Create your models here.

class Arrival(models.Model):
    vest_number = models.IntegerField(unique=True)
    arrival_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.vest_number) 
