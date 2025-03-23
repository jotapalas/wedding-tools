from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.abstract import UUIDModel, TimestampModel


class Guest(UUIDModel, TimestampModel):
    """
    Guest model
    """
    class AttendingStatusChoices(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')
        DIDNT_RESPOND = 2, _('Didn\'t respond')

    class RelationshipChoices(models.IntegerChoices):
        FRIEND = 0, _('Friend')
        FAMILY = 1, _('Family')
        COLLEAGUE = 2, _('Colleague')
        OTHER = 3, _('Other')

    class InvitedByChoices(models.IntegerChoices):
        BRIDE = 0, _('Bride')
        GROOM = 1, _('Groom')
        BOTH = 2, _('Both')

    class AgeGroupChoices(models.IntegerChoices):
        CHILD = 0, _('Child')
        TEENAGER = 1, _('Teenager')
        YOUNG_ADULT = 2, _('Young adult')
        ADULT = 3, _('Adult')
        ELDER = 4, _('Elder')

    first_name = models.CharField(
        max_length=32,
        help_text=_('First name')
    )
    last_name = models.CharField(
        max_length=32,
        help_text=_('Last name')
    )
    nickname = models.CharField(
        max_length=16,
        help_text=_('Nickname'),
        blank=True,
        default=''
    )
    email = models.EmailField(
        max_length=64,
        help_text=_('Email'),
        blank=True,
        default=''
    )
    phone = models.CharField(
        max_length=16,
        help_text=_('Phone'),
        blank=True,
        default=''
    )
    attending = models.IntegerField(
        help_text=_('Is attending?'),
        choices=AttendingStatusChoices.choices,
        default=AttendingStatusChoices.DIDNT_RESPOND,
    )

    # Group
    group = models.ForeignKey(
        'GuestGroup',
        on_delete=models.PROTECT,
        related_name='guests',
        help_text=_('Guest group'),
        null=True,
        blank=True,
    )

    # Relevant info
    info = models.TextField(
        help_text=_('Relevant notes about the guest'),
        blank=True,
        default=''
    )
    invited_by = models.IntegerField(
        help_text=_('Who invited the guest'),
        choices=InvitedByChoices.choices,
        default=InvitedByChoices.BOTH
    )
    relationship = models.IntegerField(
        help_text=_('Relationship with the couple'),
        choices=RelationshipChoices.choices,
        default=RelationshipChoices.OTHER
    )
    age_group = models.IntegerField(
        help_text=_('Age group'),
        choices=AgeGroupChoices.choices,
        default=AgeGroupChoices.ADULT
    )
    attending_probability = models.FloatField(
        help_text=_('Probability of attending'),
        default=0.0,
        choices=[
            (i/10, f'{round(100 * i/10)}%')
            for i in range(11)
        ]
    )
    open_bar = models.BooleanField(
        help_text=_('Will attend to the open bar'),
        default=True
    )
    is_vegan = models.BooleanField(
        help_text=_('Is vegan'),
        default=False
    )
    is_vegetarian = models.BooleanField(
        help_text=_('Is vegetarian'),
        default=False
    )

    class Meta:
        verbose_name = _('Guest')
        verbose_name_plural = _('Guests')
        unique_together = ['first_name', 'last_name']
        ordering = ['group', 'first_name', 'last_name']


    def __str__(self):
        return f'{self.first_name} {self.last_name}{f" ({self.nickname})" if self.nickname else ""}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def same_group_guests(self):
        return self.group.guests.all() if self.group else []
    
    def save(self, *args, **kwargs):
        prev = Guest.objects.filter(pk=self.pk).first()

        super().save(*args, **kwargs)

        # Update previous group if it's different
        if prev and prev.group and prev.group != self.group:
            if prev.group.is_empty:
                prev.group.delete()
            else:
                if prev.group.name == self.full_name:
                    prev.group.name = None
                prev.group.save()

        if self.group:
            self.group.save()


class GuestGroup(UUIDModel, TimestampModel):
    """
    Guest group model
    """
    name = models.CharField(
        max_length=64,
        help_text=_('Group name'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Guest group')
        verbose_name_plural = _('Guest groups')

    def __str__(self):
        return self.name

    @property
    def count(self):
        return self.guests.count()
    
    @property
    def attending(self):
        return self.guests.filter(attending=Guest.AttendingStatusChoices.YES).count()

    @property
    def is_empty(self):
        return self.count == 0

    def save(self, *args, **kwargs):
        if not self.name:
            first_guest = self.guests.first()
            first_guest.full_name if first_guest else self.id
        super().save(*args, **kwargs)
