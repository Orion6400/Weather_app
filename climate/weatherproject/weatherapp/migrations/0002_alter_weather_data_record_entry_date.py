# Generated by Django 3.2.5 on 2022-03-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather_data',
            name='record_entry_date',
            field=models.DateTimeField(default=True),
        ),
    ]