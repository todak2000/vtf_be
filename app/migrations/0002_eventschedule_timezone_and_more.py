# Generated by Django 4.1.2 on 2022-10-12 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventschedule",
            name="timezone",
            field=models.CharField(
                choices=[
                    ("PST", "PST"),
                    ("GMT", "GMT"),
                    ("IST", "IST"),
                    ("BST", "BST"),
                    ("WAT", "WAT"),
                    ("CET", "CET"),
                ],
                default="PST",
                max_length=20,
                verbose_name="Time Zone",
            ),
        ),
        migrations.AlterField(
            model_name="eventschedule",
            name="date_added",
            field=models.DateTimeField(),
        ),
    ]
