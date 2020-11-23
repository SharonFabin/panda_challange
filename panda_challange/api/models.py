from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=60)
    count = models.IntegerField()


class Data(models.Model):
    name = models.CharField(max_length=60)
    count = models.IntegerField()
