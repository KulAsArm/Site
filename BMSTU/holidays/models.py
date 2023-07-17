from django.db import models

# Create your models here.
class Destinations(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    tot_seats = models.IntegerField()
    occ_seats = models.IntegerField()
    def __str__(self):
        return f"{self.name}, дата заезда:{self.date}"