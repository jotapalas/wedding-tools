from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.abstract import UUIDModel, TimestampModel


class FAQ(UUIDModel, TimestampModel):
    """Model for frequently asked questions."""

    question = models.CharField(max_length=255, verbose_name=_("Question"))
    answer = models.TextField(verbose_name=_("Answer"))

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        ordering = ["-created_at"]

    def __str__(self):
        return self.question
