from django.apps import AppConfig


class ArrivalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arrivals'

    def ready(self):
        import arrivals.signals