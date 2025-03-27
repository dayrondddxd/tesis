from django.apps import AppConfig


class IntegrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'integration'

    def ready(self):
        import integration.signals  # Importar las señales

