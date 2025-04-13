from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WeddingInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wedding_info'
    verbose_name = _('Wedding Info')
