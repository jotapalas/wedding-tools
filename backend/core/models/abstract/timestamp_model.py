from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class TimestampModel(models.Model):
    """
    Adds created_at and last_modified_at fields to models
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
        help_text=_('Date and time where this record was created.')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at'),
        help_text=_('Date and time of this record last edition.')
    )

    class Meta:
        abstract = True


    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
