from __future__ import unicode_literals

from django.db import models

# Create your models
class Measurment(models.Model):
    area = models.TextField(max_length=1, primary_key=True)
    station = models.TextField(max_length=50, primary_key=True)
    date_field = models.DateField(primary_key=True)
    time_field = models.TimeField(primary_key=True)
    '''area = models.TextField(max_length=1)
    station = models.TextField(max_length=50)
    date_field = models.DateField()
    time_field = models.TimeField()'''
    m1 = models.FloatField()
    m2 = models.FloatField()
    m3 = models.FloatField()
    m4 = models.FloatField()


class Area_inform(models.Model):
    areas = models.TextField(max_length=1, primary_key=True)
    station = models.TextField(max_length=50, primary_key=True)
    elevation = models.FloatField()
    point_x = models.FloatField()
    point_y = models.FloatField()

class Areas(models.Model):
    area =  models.TextField(max_length=1, primary_key=True)
    area_name = models.TextField(max_length=50)