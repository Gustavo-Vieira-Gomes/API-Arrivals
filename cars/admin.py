from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'team', 'car_identification', 'car_model', 'cars_per_team', )
    search_fields = ('full_name', 'phone_number', 'team', 'car_identification', )