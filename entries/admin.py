from django.contrib import admin
from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'boat_class','sex_category', 'age_category', 'vest_number',)
    search_fields = ('name1', 'boat_class','sex_category', 'age_category', 'vest_number',)