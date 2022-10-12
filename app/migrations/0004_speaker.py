# Generated by Django 4.1.2 on 2022-10-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_eventschedule_date_added"),
    ]

    operations = [
        migrations.CreateModel(
            name="Speaker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "firstname",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Firstname"
                    ),
                ),
                (
                    "lastname",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Lastname"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=90, null=True, unique=True, verbose_name="Email"
                    ),
                ),
                ("password", models.TextField(max_length=200, verbose_name="Password")),
                ("date_added", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "Speakers_table",
            },
        ),
    ]
