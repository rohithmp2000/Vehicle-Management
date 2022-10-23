from django.db import models

# Create your models here.
class Vehicle(models.Model):
    Vehicle_number=models.CharField(max_length=10)
    Vehicle_type_choice= (
    ("2", "Two Wheeler"),
    ("3", "Three Wheeler"),
    ("4", "Four Wheeler"),
)
    Vehicle_type = models.CharField(choices=Vehicle_type_choice,max_length=1)
    Vehicle_model=models.CharField(max_length=20)
    Vehicle_description=models.TextField()