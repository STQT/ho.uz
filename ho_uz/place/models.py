import os
from datetime import datetime
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="places")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    size = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="places/")
    services = models.ManyToManyField("Services", blank=True)

    def __str__(self):
        return self.name


def get_shot_upload_path(instance, filename):
    today = datetime.today()
    return os.path.join('shots', str(today.year), str(today.month), str(today.day), filename)


class PlaceShots(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="shots")
    photo = models.ImageField(upload_to=get_shot_upload_path)

    def __str__(self):
        return f"#{self.id}"
