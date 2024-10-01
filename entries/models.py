from django.db import models


class Entry(models.Model):

    CATEGORY_CHOICES = [
        ('OC6', 'OC6'),
        ('V6', 'V6'),
        ('OC2', 'OC2'),
        ('V2', 'V2'),
        ('OC1', 'OC1'),
        ('V1', 'V1'),
        ('TUR', 'Turismo'),
        ('OCI', 'Oceânico Individual'),
        ('OCD', 'Oceânico Duplo'),
        ('LFS', 'Lifesaving'),
        ('SFKI', 'Surfski Individual'),
        ('SFKD', 'Surfski Duplo'),
        ('PCD', 'Para-Canoagem'),
    ]

    SEX_CATEGORY_CHOICES = [
        ('MALE', 'Masculino'),
        ('FEMALE', 'Feminino'),
        ('MIXED', 'Misto')
    ]

    AGE_CATEGORY_CHOICES = [
        ('OPEN', 'OPEN'),
        ('+40', '+40'),
        ('SUB 20', 'SUB 20'),
        ('SENIOR', 'SENIOR'),
        ('MASTER A', 'MASTER A'),
        ('MASTER B', 'MASTER B'),
    ]


    name1 = models.CharField(max_length=80, unique=True)
    name2 = models.CharField(max_length=80, blank=True, null=True)
    name3 = models.CharField(max_length=80, blank=True, null=True)
    name4 = models.CharField(max_length=80, blank=True, null=True)
    name5 = models.CharField(max_length=80, blank=True, null=True)
    name6 = models.CharField(max_length=80, blank=True, null=True)
    boat_class = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    sex_category = models.CharField(max_length=10, choices=SEX_CATEGORY_CHOICES)
    age_category = models.CharField(max_length=15, choices=AGE_CATEGORY_CHOICES)
    vest_number = models.IntegerField()

    def __str__(self) -> str:
        return self.name1
