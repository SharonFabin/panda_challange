from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_type = models.CharField(max_length=60)
    data = models.CharField(max_length=60)
    timestamp = models.CharField(max_length=60)


class EventCount(models.Model):
    event_type = models.CharField(max_length=60)
    count = models.IntegerField()
