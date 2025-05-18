from django.apps import AppConfig


class CinemaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cinema_core"

    def ready(self) -> None:
        from cinema_core import signals  # noqa
