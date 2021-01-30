from django.apps import AppConfig


class FuturesConfig(AppConfig):
    name = 'futures'

    def ready(self):
        import futures.signals
