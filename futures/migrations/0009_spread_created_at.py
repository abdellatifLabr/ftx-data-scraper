# Generated by Django 3.1.5 on 2021-01-30 11:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('futures', '0008_spread'),
    ]

    operations = [
        migrations.AddField(
            model_name='spread',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]