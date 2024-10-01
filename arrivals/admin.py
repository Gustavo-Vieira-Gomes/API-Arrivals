from django.contrib import admin
from .models import Arrival
# Register your models here.

@admin.register(Arrival)
class ArrivalAdmin(admin.ModelAdmin):
    list_display = ('vest_number', 'arrival_time',)
    search_fields = ('vest_number',)
