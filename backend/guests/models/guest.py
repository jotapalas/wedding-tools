import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

from core.models.abstract import UUIDModel, TimestampModel


class Guest(UUIDModel, TimestampModel):
    """
    Guest model
    """
    class AttendingStatusChoices(models.IntegerChoices):
        DIDNT_RESPOND = -1, _('Didn\'t respond')
        NO = 0, _('No')
        YES = 1, _('Yes')
        MAYBE = 2, _('Maybe')

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

    class SpecialDietChoices(models.TextChoices):
        VEGETARIAN = 'vegetarian', _('Vegetarian')
        VEGAN = 'vegan', _('Vegan')
        CHILD_FOOD = 'child_food', _('Child food')
        PREGNANT = 'pregnant', _('Pregnant')

    first_name = models.CharField(
        max_length=32,
        verbose_name=_('First name')
    )
    last_name = models.CharField(
        max_length=32,
        verbose_name=_('Last name')
    )
    nickname = models.CharField(
        max_length=16,
        verbose_name=_('Nickname'),
        blank=True,
        default=''
    )
    email = models.EmailField(
        max_length=64,
        verbose_name=_('Email'),
        blank=True,
        default=''
    )
    phone = models.CharField(
        max_length=16,
        verbose_name=_('Phone'),
        blank=True,
        default=''
    )
    attending = models.IntegerField(
        verbose_name=_('Is attending?'),
        choices=AttendingStatusChoices.choices,
        default=AttendingStatusChoices.DIDNT_RESPOND,
    )
    pre_wedding = models.IntegerField(
        verbose_name=_('Pre-wedding attendance'),
        choices=AttendingStatusChoices.choices,
        default=AttendingStatusChoices.DIDNT_RESPOND,
    )

    # Group
    group = models.ForeignKey(
        'GuestGroup',
        on_delete=models.PROTECT,
        related_name='guests',
        verbose_name=_('Group'),
        help_text=_('Guest group, if any'),
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
        verbose_name=_('Invited by'),
        help_text=_('Who invited the guest'),
        choices=InvitedByChoices.choices,
        default=InvitedByChoices.BOTH
    )
    relationship = models.IntegerField(
        verbose_name=_('Relationship'),
        help_text=_('Relationship with the couple'),
        choices=RelationshipChoices.choices,
        default=RelationshipChoices.OTHER
    )
    age_group = models.IntegerField(
        verbose_name=_('Age group'),
        choices=AgeGroupChoices.choices,
        default=AgeGroupChoices.ADULT
    )
    attending_probability = models.FloatField(
        verbose_name=_('Probability of attending'),
        default=0.0,
        choices=[
            (i/10, f'{round(100 * i/10)}%')
            for i in range(11)
        ]
    )
    open_bar = models.BooleanField(
        verbose_name=_('Open bar'),
        help_text=_('Will attend to the open bar'),
        default=True
    )
    special_diet = models.CharField(
        max_length=16,
        verbose_name=_('Special diet'),
        choices=SpecialDietChoices.choices,
        blank=True,
        default=''
    )
    allergies = models.CharField(
        max_length=128,
        verbose_name=_('Other allergies'),
        blank=True,
        default=''
    )
    needs_transport = models.BooleanField(
        verbose_name=_('Needs transport'),
        default=False
    )
    needs_accommodation = models.BooleanField(
        verbose_name=_('Needs accomodation'),
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
        return self.group.guests.exclude(pk=self.pk) if self.group else []
    
    @property
    def personalised_url(self):
        base_url = os.getenv('BASE_URL', '')
        return f'{base_url}?guestId={self.id.hex}'

    @property
    def is_vegan(self):
        return self.special_diet == self.SpecialDietChoices.VEGAN

    @property
    def is_vegetarian(self):
        return self.special_diet == self.SpecialDietChoices.VEGETARIAN
    
    def save(self, *args, **kwargs):
        if self.attending == self.AttendingStatusChoices.YES:
            self.attending_probability = 1
        if self.attending == self.AttendingStatusChoices.NO:
            self.attending_probability = 0
        
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
        verbose_name=_('Group name'),
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
