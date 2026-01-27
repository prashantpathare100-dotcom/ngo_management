from django.db import models

class Donation(models.Model):
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class Volunteer(models.Model):
    name = models.CharField(max_length=100)

class Event(models.Model):
    title = models.CharField(max_length=200)
