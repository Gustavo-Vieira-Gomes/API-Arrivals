from django.contrib import admin
from .models import Start


@admin.register(Start)
class StartAdmin(admin.ModelAdmin):
    list_display = ('category', 'start_time',)
    search_fields = ('category', )
