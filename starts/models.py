from django.db import models


class Start(models.Model):

    CATEGORY_CHOICES = [
        ('OC6', ''),
        ('GERAL', ''),
        ('JUNIORES', '')
    ]

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, unique=True)
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.category
