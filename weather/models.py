from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()

    def __str__(self):
        return self.city

