from django.db import models


class Entry(models.Model):

    name1 = models.CharField(max_length=80, unique=True)
    name2 = models.CharField(max_length=80, blank=True, null=True)
    name3 = models.CharField(max_length=80, blank=True, null=True)
    name4 = models.CharField(max_length=80, blank=True, null=True)
    name5 = models.CharField(max_length=80, blank=True, null=True)
    name6 = models.CharField(max_length=80, blank=True, null=True)
    boat_class = models.CharField(max_length=80)
    sex_category = models.CharField(max_length=80)
    age_category = models.CharField(max_length=80)
    vest_number = models.IntegerField()

    def __str__(self) -> str:
        return self.name1
