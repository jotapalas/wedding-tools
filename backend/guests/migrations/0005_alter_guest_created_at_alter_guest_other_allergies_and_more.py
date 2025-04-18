# Generated by Django 5.0.6 on 2025-04-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_guest_common_allergies_guest_other_allergies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time where this record was created.', verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='other_allergies',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Other allergies'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time of this record last edition.', verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='guestgroup',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time where this record was created.', verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='guestgroup',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time of this record last edition.', verbose_name='Updated at'),
        ),
    ]
