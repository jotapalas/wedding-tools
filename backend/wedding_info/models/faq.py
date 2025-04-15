from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.abstract import UUIDModel, TimestampModel


class FAQ(UUIDModel, TimestampModel):
    """Model for frequently asked questions."""

    question = models.CharField(max_length=255, verbose_name=_("Question"))
    answer = models.TextField(verbose_name=_("Answer"))
    include_moodboard = models.BooleanField(
        default=False,
        verbose_name=_("Include moodboard"),
        help_text=_("Include the moodboard in this FAQ"),
    )
    order = models.PositiveIntegerField(
        default=0, verbose_name=_("Order"), help_text=_("Order of the FAQ")
    )

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        ordering = ["order"]

    def __str__(self):
        return self.question
