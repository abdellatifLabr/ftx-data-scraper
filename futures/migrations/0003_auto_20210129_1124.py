# Generated by Django 3.1.5 on 2021-01-29 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futures', '0002_future_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='future',
            old_name='change_1h',
            new_name='change1h',
        ),
        migrations.RenameField(
            model_name='future',
            old_name='change_24h',
            new_name='change24h',
        ),
        migrations.RenameField(
            model_name='future',
            old_name='volume_usd_24h',
            new_name='volume_usd24h',
        ),
    ]
