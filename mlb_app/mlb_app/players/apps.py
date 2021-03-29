from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PlayersConfig(AppConfig):
    name = "mlb_app.players"
    verbose_name = _("Players")

    def ready(self):
        try:
            import mlb_app.players.signals  # noqa F401
        except ImportError:
            pass
