from django.db import models

# Create your models here.

class CarsModel(models.Model):
    carname=models.CharField(max_length=64)
    brand=models.CharField(max_length=64)
    year=models.IntegerField()
    owner=models.CharField(max_length=64)

    def __str__(self):
        return self.owner