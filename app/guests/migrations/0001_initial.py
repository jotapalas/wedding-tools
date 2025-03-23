# Generated by Django 5.0.6 on 2025-03-23 11:32

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestGroup',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time where this record was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of this record last edition.')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID generated by system', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Group name', max_length=64, null=True)),
            ],
            options={
                'verbose_name': 'Guest group',
                'verbose_name_plural': 'Guest groups',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time where this record was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of this record last edition.')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID generated by system', primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First name', max_length=32)),
                ('last_name', models.CharField(help_text='Last name', max_length=32)),
                ('nickname', models.CharField(blank=True, help_text='Nickname', max_length=16, null=True)),
                ('email', models.EmailField(help_text='Email', max_length=64)),
                ('phone', models.CharField(help_text='Phone', max_length=16)),
                ('attending', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, "Didn't respond")], default=2, help_text='Is attending?', null=True)),
                ('group', models.ForeignKey(blank=True, help_text='Guest group', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='guests', to='guests.guestgroup')),
            ],
            options={
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
                'ordering': ['group', 'first_name', 'last_name'],
            },
        ),
    ]
