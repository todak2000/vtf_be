# Generated by Django 4.1.2 on 2022-10-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_eventschedule_timezone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventschedule",
            name="date_added",
            field=models.DateTimeField(auto_now=True),
        ),
    ]