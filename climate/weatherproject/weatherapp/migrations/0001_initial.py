# Generated by Django 3.2.5 on 2022-03-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weather_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('coordinates', models.CharField(max_length=255)),
                ('temp', models.CharField(max_length=255)),
                ('real_temp_feel', models.CharField(max_length=255)),
                ('pressure', models.CharField(max_length=255)),
                ('humidity', models.CharField(max_length=255)),
                ('wind_speed', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('record_entry_date', models.DateTimeField()),
            ],
        ),
    ]
