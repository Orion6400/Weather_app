# Generated by Django 4.0.4 on 2022-05-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0003_alter_weather_data_record_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather_data',
            name='record_entry_date',
            field=models.CharField(max_length=255),
        ),
    ]