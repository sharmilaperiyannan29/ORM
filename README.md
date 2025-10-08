# Ex02 Django ORM Web Application
## Date:18/09/2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
"""
model.py
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

admin.py

from django.contrib import admin
from .models import car,carAdmin
admin.site.register(car,carAdmin)



## OUTPUT

<img width="1906" height="1072" alt="Screenshot 2025-09-19 213355" src="https://github.com/user-attachments/assets/c2c2fabb-eb41-4aee-aae0-55e937285469" />


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
