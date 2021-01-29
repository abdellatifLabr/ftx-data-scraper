# Generated by Django 3.1.5 on 2021-01-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futures', '0003_auto_20210129_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='future',
            name='predicted_expiration_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='future',
            name='strike_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
