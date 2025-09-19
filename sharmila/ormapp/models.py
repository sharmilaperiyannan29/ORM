from django.db import models
from django.contrib import admin
class car(models.Model):
    carid=models.IntegerField()
    carname=models.CharField(max_length=100)
    colour=models.CharField(max_length=100)
    year=models.IntegerField()
    rating=models.FloatField()

class carAdmin(admin.ModelAdmin):
    list_display=('carid','carname','colour','year','rating')



