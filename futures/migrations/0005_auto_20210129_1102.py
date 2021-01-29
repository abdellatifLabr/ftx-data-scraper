# Generated by Django 3.1.5 on 2021-01-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futures', '0004_auto_20210129_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='future',
            name='change1h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='change24h',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='change_bod',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='enabled',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='expired',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='expiry_description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='imf_factor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='index',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='last',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='lower_bound',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='margin_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='mark',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='next_funding_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='next_funding_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='open_interest',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='perpetual',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='position_limit_weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='post_only',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='price_increment',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='size_increment',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='underlying_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='upper_bound',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='volume',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='future',
            name='volume_usd24h',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
