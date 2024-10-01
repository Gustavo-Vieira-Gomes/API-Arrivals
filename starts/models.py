from django.db import models


class Start(models.Model):

    CATEGORY_CHOICES = [
        ('OC6', ''),
        ('V6', ''),
        ('OC2', ''),
        ('V2', ''),
        ('OC1', ''),
        ('V1', ''),
        ('Turismo', ''),
        ('Oceânico individual', ''),
        ('Oceânico duplo', ''),
        ('Lifesaving', ''),
        ('Surfski individual', ''),
        ('Surfski duplo', ''),
        ('Para-Canoagem', ''),
    ]

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.category