# Generated by Django 3.1.5 on 2021-01-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Future',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.FloatField()),
                ('bid', models.FloatField()),
                ('change_1h', models.FloatField()),
                ('change_24h', models.FloatField()),
                ('change_bod', models.FloatField()),
                ('description', models.TextField()),
                ('enabled', models.BooleanField()),
                ('expired', models.BooleanField()),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('expiry_description', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=50)),
                ('imf_factor', models.FloatField()),
                ('index', models.FloatField()),
                ('last', models.FloatField()),
                ('lower_bound', models.FloatField()),
                ('margin_price', models.FloatField()),
                ('mark', models.FloatField()),
                ('move_start', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('perpetual', models.BooleanField()),
                ('position_limit_weight', models.FloatField()),
                ('post_only', models.BooleanField()),
                ('price_increment', models.FloatField()),
                ('size_increment', models.FloatField()),
                ('type', models.CharField(max_length=50)),
                ('underlying', models.CharField(max_length=50)),
                ('underlying_description', models.TextField()),
                ('upper_bound', models.FloatField()),
                ('volume', models.FloatField()),
                ('volume_usd_24h', models.FloatField()),
                ('next_funding_rate', models.FloatField()),
                ('next_funding_time', models.DateTimeField()),
                ('open_interest', models.FloatField()),
            ],
        ),
    ]