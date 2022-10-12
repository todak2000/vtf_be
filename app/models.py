from django.db import models
from django.utils import timezone
import json
import datetime

# Create your models here.


def format_data(data):
    formated_data = [item.long() for item in data]
    return formated_data


# specifying timezone choices
TIMEZONE_CHOICES = (
    ("PST", "PST"),
    ("GMT", "GMT"),
    ("IST", "IST"),
    ("BST", "BST"),
    ("WAT", "WAT"),
    ("CET", "CET"),
)

# ISACA Event Schedule Model


class EventSchedule(models.Model):
    class Meta:
        db_table = "EventSchedule_Table"

    title = models.TextField(verbose_name="Event Title", null=True, blank=True)
    message = models.TextField(
        verbose_name="Event Synopsis", null=True, blank=True)
    day = models.DateField(default=timezone.now,
                           verbose_name="Day of Event", null=True, blank=True)
    timezone = models.CharField(
        verbose_name="Time Zone", max_length=20, choices=TIMEZONE_CHOICES, default="PST")
    time = models.TimeField(auto_now=False, auto_now_add=False,
                            verbose_name="Event Time", null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def long(self):
        day = self.day.strftime("%d %b, %Y")
        month = self.day.strftime("%B")
        time = self.time.strftime('%-I:%M %p') + " " + str(self.timezone)
        today = datetime.date.today()
        if self.day >= today:
            ongoing = True
        else:
            ongoing = False
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "day": day,
            "ongoing": ongoing,
            "month": month,
            "time": time,
        }

    def __str__(self):
        return json.dumps(self.long())

# VTF Speaker Users DB


class Speaker(models.Model):
    class Meta:
        db_table = "Speakers_table"

    firstname = models.CharField(
        max_length=30, verbose_name="Firstname", blank=True, null=True)
    lastname = models.CharField(
        max_length=30, verbose_name="Lastname", blank=True, null=True)
    email = models.EmailField(
        max_length=90, unique=True, verbose_name="Email", null=True)
    password = models.TextField(max_length=200, verbose_name="Password")
    date_added = models.DateTimeField(auto_now=True)

    def long(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "date_registered": self.date_added,
        }

    def __str__(self):
        return json.dumps(self.long())
