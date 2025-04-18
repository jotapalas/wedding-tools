# Generated by Django 5.0.6 on 2025-04-13 13:53

from django.db import migrations, models


def update_attending_field(apps, schema_editor):
    Guest = apps.get_model('guests', 'Guest')
    # Update the default value for the 'attending' field
    Guest.objects.filter(attending=2).update(attending=-1)

def rollback_attending_field(apps, schema_editor):
    Guest = apps.get_model('guests', 'Guest')
    # Update the default value for the 'attending' field
    Guest.objects.filter(attending=-1).update(attending=2)


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0006_remove_guest_common_allergies_remove_guest_is_vegan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='pre_wedding',
            field=models.IntegerField(choices=[(-1, "Didn't respond"), (0, 'No'), (1, 'Yes'), (2, 'Maybe')], default=-1, verbose_name='Pre-wedding attendance'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='attending',
            field=models.IntegerField(choices=[(-1, "Didn't respond"), (0, 'No'), (1, 'Yes'), (2, 'Maybe')], default=-1, verbose_name='Is attending?'),
        ),
        migrations.RunPython(
            update_attending_field,
            rollback_attending_field
        ),
    ]
